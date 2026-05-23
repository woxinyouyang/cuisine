"""
真实菜肴图片下载器
来源: 下厨房 (xiachufang.com) + 百度图片 (Baidu Image)
"""

import json, os, re, time, requests, concurrent.futures

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, "dishes.json")
IMAGES_DIR = os.path.join(BASE_DIR, "images")
os.makedirs(IMAGES_DIR, exist_ok=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "zh-CN,zh;q=0.9",
}


def search_xiachufang(term):
    """从下厨房搜索菜肴图片"""
    url = "https://www.xiachufang.com/search/"
    params = {"keyword": term}
    try:
        resp = requests.get(url, params=params, headers=HEADERS, timeout=10)
        if resp.status_code != 200:
            return None
        # 提取真实菜肴图片
        imgs = re.findall(r'<img[^>]+src="(https?://[^"]+\.(?:jpg|jpeg|png)[^"]*)"', resp.text)
        # 过滤掉图标和头像
        for img in imgs:
            if "avatar" in img.lower() or "logo" in img.lower() or "story" in img.lower():
                continue
            if "chuimg" in img or "xiachufang" in img:
                # Clean URL
                clean = re.sub(r'\?.*', '', img)
                return clean
        return None
    except requests.RequestException:
        return None


def search_baidu_image(term):
    """从百度图片搜索获取"""
    url = "https://image.baidu.com/search/acjson"
    headers = {**HEADERS, "Referer": "https://image.baidu.com/"}
    params = {"tn": "resultjson_com", "word": term, "pn": 0, "rn": 5}
    try:
        resp = requests.get(url, params=params, headers=headers, timeout=10)
        if resp.status_code != 200:
            return None
        data = resp.json()
        for item in data.get("data", []):
            thumb = item.get("thumbURL", "")
            middle = item.get("middleURL", "")
            img_url = middle or thumb
            if img_url and len(img_url) > 10:
                return img_url
        return None
    except (requests.RequestException, json.JSONDecodeError):
        return None


def get_image(term):
    """多源获取图片"""
    # 1. 下厨房 (优先，真实菜肴图多)
    url = search_xiachufang(term)
    if url:
        return url

    # 2. 百度图片
    url = search_baidu_image(term)
    if url:
        return url

    return None


def download(url, filepath):
    """下载图片"""
    if os.path.exists(filepath) and os.path.getsize(filepath) > 2000:
        return True
    try:
        resp = requests.get(url, headers=HEADERS, timeout=15, stream=True)
        if resp.status_code == 200:
            content = resp.content
            if len(content) >= 3000:
                with open(filepath, "wb") as f:
                    f.write(content)
                return True
    except requests.RequestException:
        pass
    return False


def main():
    print("=== 真实菜肴图片下载器 ===\n")

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    dishes = data["dishes"]
    total = len(dishes)
    success = 0
    fail = 0

    for i, dish in enumerate(dishes, 1):
        name = dish["name"]
        dish_id = dish["id"]
        jpg_path = os.path.join(IMAGES_DIR, f"{dish_id}.jpg")
        svg_path = os.path.join(IMAGES_DIR, f"{dish_id}.svg")

        # 已有真实JPG则跳过
        if os.path.exists(jpg_path) and os.path.getsize(jpg_path) > 2000:
            # 同时删除SVG占位图
            if os.path.exists(svg_path):
                os.remove(svg_path)
            continue

        print(f"[{i}/{total}] {name}...", end=" ", flush=True)
        img_url = get_image(name)

        if img_url and download(img_url, jpg_path):
            success += 1
            print("OK")
            # 删除SVG
            if os.path.exists(svg_path):
                os.remove(svg_path)
        else:
            fail += 1
            print("x")

        # 礼貌延迟
        time.sleep(0.5)

    # 更新 dishes.json
    updated = 0
    for dish in dishes:
        did = dish["id"]
        jp = os.path.join(IMAGES_DIR, f"{did}.jpg")
        sp = os.path.join(IMAGES_DIR, f"{did}.svg")
        if os.path.exists(jp) and os.path.getsize(jp) > 2000:
            dish["image"] = f"images/{did}.jpg"
            updated += 1
        elif os.path.exists(sp):
            dish["image"] = f"images/{did}.svg"

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\n=== Done ===")
    print(f"Downloaded: {success}")
    print(f"Failed: {fail}")
    print(f"Updated dishes.json: {updated}")


if __name__ == "__main__":
    main()
