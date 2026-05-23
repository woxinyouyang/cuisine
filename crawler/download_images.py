"""
菜肴图片下载器 —— 从百度百科直接提取菜肴图片
"""

import json
import os
import re
import time
import random
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, "dishes.json")
IMAGES_DIR = os.path.join(BASE_DIR, "images")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}

os.makedirs(IMAGES_DIR, exist_ok=True)


def get_baike_image(name):
    """从百度百科页面提取主图"""
    encoded_name = requests.utils.quote(name)
    url = f"https://baike.baidu.com/item/{encoded_name}"
    try:
        resp = requests.get(url, headers=HEADERS, timeout=10)
        if resp.status_code != 200:
            return None
        soup = BeautifulSoup(resp.text, "html.parser")

        # 百度百科的图片通常在 .summary-pic 或 .basicInfo-item 中
        candidates = []

        # 1. 主图区域
        for img in soup.select(".summary-pic img"):
            src = img.get("src") or img.get("data-src") or ""
            if src:
                candidates.append(src)

        # 2. 卡片式新页面
        for img in soup.select(".basicInfo-item img"):
            src = img.get("src") or img.get("data-src") or ""
            if src:
                candidates.append(src)

        # 3. 任意大图
        for img in soup.select("img[src*=\"baike\"]"):
            src = img.get("src") or img.get("data-src") or ""
            if src and ("pic" in src or "img" in src):
                if "logo" not in src and "icon" not in src:
                    candidates.append(src)

        if not candidates:
            return None

        img_url = candidates[0]
        if img_url.startswith("//"):
            img_url = "https:" + img_url
        elif img_url.startswith("/"):
            img_url = "https://baike.baidu.com" + img_url
        return img_url

    except requests.RequestException:
        return None


def download_image(url, filepath):
    """下载图片到本地"""
    if os.path.exists(filepath) and os.path.getsize(filepath) > 1000:
        return True
    try:
        resp = requests.get(url, headers=HEADERS, timeout=15, stream=True)
        if resp.status_code == 200:
            content = resp.content
            if len(content) > 2000:
                with open(filepath, "wb") as f:
                    f.write(content)
                return True
    except requests.RequestException:
        pass
    return False


def main():
    print("=== 中华古典菜肴百科 - 图片下载器 ===\n")

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    dishes = data["dishes"]
    total = len(dishes)
    success = 0
    skipped = 0

    for i, dish in enumerate(dishes, 1):
        dish_id = dish["id"]
        filepath = os.path.join(IMAGES_DIR, f"{dish_id}.jpg")
        name = dish["name"]

        if os.path.exists(filepath) and os.path.getsize(filepath) > 1000:
            skipped += 1
            continue

        print(f"[{i}/{total}] {name}...", end=" ", flush=True)

        img_url = get_baike_image(name)
        if img_url and download_image(img_url, filepath):
            success += 1
            print("OK")
        else:
            print("x")
            # Try alternative: search for simplified name or common name variants

        time.sleep(random.uniform(0.8, 1.5))

    print(f"\n=== Done ===")
    print(f"Total: {total}")
    print(f"Downloaded: {success}")
    print(f"Skipped (existing): {skipped}")
    print(f"Missing: {total - success - skipped}")


if __name__ == "__main__":
    main()
