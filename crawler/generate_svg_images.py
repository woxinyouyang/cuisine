"""
菜肴图片生成器 —— 生成中国风SVG占位图
每道菜一张专属图，含菜名和菜系标签
"""

import json
import os
import re
import hashlib

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, "dishes.json")
IMAGES_DIR = os.path.join(BASE_DIR, "images")

os.makedirs(IMAGES_DIR, exist_ok=True)

# 根据菜系分配配色
CUISINE_COLORS = {
    "川菜": {"bg1": "#C41E3A", "bg2": "#8B1A1A", "text": "#FFF8F0", "accent": "#FFD700"},
    "鲁菜": {"bg1": "#2F4F2F", "bg2": "#1A3A1A", "text": "#FFF8F0", "accent": "#D4A574"},
    "粤菜": {"bg1": "#1A5276", "bg2": "#0E3A5C", "text": "#FFF8F0", "accent": "#F0E68C"},
    "苏菜": {"bg1": "#5B3A29", "bg2": "#3C2415", "text": "#FFF8F0", "accent": "#E8D5B7"},
    "浙菜": {"bg1": "#2C3E50", "bg2": "#1A2A38", "text": "#FFF8F0", "accent": "#AED6F1"},
    "闽菜": {"bg1": "#6C3483", "bg2": "#4A235A", "text": "#FFF8F0", "accent": "#D7BDE2"},
    "湘菜": {"bg1": "#B03A2E", "bg2": "#7B241C", "text": "#FFF8F0", "accent": "#F9E79F"},
    "徽菜": {"bg1": "#1B4F72", "bg2": "#0E3250", "text": "#FFF8F0", "accent": "#A3E4D7"},
    "宫廷菜": {"bg1": "#7D6608", "bg2": "#4D4008", "text": "#FFF8F0", "accent": "#FFD700"},
    "民间古典": {"bg1": "#616A6B", "bg2": "#424949", "text": "#FFF8F0", "accent": "#D5D8DC"},
}

DEFAULT_COLOR = {"bg1": "#8B5A2B", "bg2": "#5C3A28", "text": "#FFF8F0", "accent": "#D4A574"}


def generate_svg(name, pinyin, cuisine):
    """为一道菜生成中国风SVG"""
    colors = CUISINE_COLORS.get(cuisine, DEFAULT_COLOR)

    # 根据菜名生成一个装饰元素的位置偏移
    seed = sum(ord(c) for c in name)
    circle_x = 120 + (seed % 160)
    circle_y = 80 + (seed % 60)
    circle_r = 30 + (seed % 30)

    # 生成装饰性山水/云纹
    lines = []
    for i in range(3):
        y = 30 + i * 45 + (seed % 20)
        lines.append(f'<path d="M{20 + i*20},{y} Q{100 + i*15},{y - 15 + (seed%10)} {180 - i*10},{y}" stroke="{colors["accent"]}" stroke-width="1.5" fill="none" opacity="0.4"/>')

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200">
  <defs>
    <linearGradient id="bg-{seed}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:{colors['bg1']};stop-opacity:1" />
      <stop offset="100%" style="stop-color:{colors['bg2']};stop-opacity:1" />
    </linearGradient>
    <linearGradient id="shine-{seed}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:{colors['accent']};stop-opacity:0.15" />
      <stop offset="50%" style="stop-color:{colors['accent']};stop-opacity:0.05" />
      <stop offset="100%" style="stop-color:{colors['accent']};stop-opacity:0.15" />
    </linearGradient>
  </defs>

  <!-- 背景 -->
  <rect width="300" height="200" fill="url(#bg-{seed})" rx="4"/>

  <!-- 装饰光晕 -->
  <rect width="300" height="200" fill="url(#shine-{seed})" rx="4"/>

  <!-- 装饰性圆 -->
  <circle cx="{circle_x}" cy="{circle_y}" r="{circle_r}" fill="none" stroke="{colors['accent']}" stroke-width="1" opacity="0.3"/>
  <circle cx="{circle_x + 20}" cy="{circle_y - 10}" r="{circle_r - 10}" fill="none" stroke="{colors['accent']}" stroke-width="0.8" opacity="0.2"/>

  <!-- 水墨线条 -->
  {chr(10).join(lines)}

  <!-- 餐具图标 -->
  <text x="150" y="85" text-anchor="middle" font-size="36" opacity="0.3" fill="{colors['accent']}">&#x1F372;</text>

  <!-- 菜名 -->
  <text x="150" y="130" text-anchor="middle" font-family="'Ma Shan Zheng','SimSun',serif" font-size="28" fill="{colors['text']}" font-weight="bold">{name}</text>

  <!-- 拼音 -->
  <text x="150" y="155" text-anchor="middle" font-family="serif" font-size="11" fill="{colors['accent']}" opacity="0.8">{pinyin}</text>

  <!-- 菜系标签 -->
  <rect x="110" y="168" width="80" height="22" rx="11" fill="{colors['accent']}" opacity="0.25"/>
  <text x="150" y="183" text-anchor="middle" font-family="serif" font-size="11" fill="{colors['accent']}">{cuisine}</text>

  <!-- 印章装饰 -->
  <rect x="260" y="12" width="24" height="24" rx="2" fill="none" stroke="{colors['accent']}" stroke-width="1" opacity="0.5" transform="rotate(8, 272, 24)"/>
  <text x="272" y="29" text-anchor="middle" font-family="serif" font-size="12" fill="{colors['accent']}" opacity="0.5">食</text>
</svg>'''
    return svg


def main():
    print("=== 菜肴SVG图片生成器 ===\n")

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    dishes = data["dishes"]
    total = len(dishes)
    generated = 0
    skipped = 0

    for i, dish in enumerate(dishes, 1):
        dish_id = dish["id"]
        svg_path = os.path.join(IMAGES_DIR, f"{dish_id}.svg")
        jpg_path = os.path.join(IMAGES_DIR, f"{dish_id}.jpg")

        # 如果已经有JPG图片则跳过
        if os.path.exists(jpg_path) and os.path.getsize(jpg_path) > 1000:
            skipped += 1
            continue

        name = dish["name"]
        pinyin = dish["pinyin"]
        cuisine = dish["cuisine"]

        svg = generate_svg(name, pinyin, cuisine)
        with open(svg_path, "w", encoding="utf-8") as f:
            f.write(svg)
        generated += 1

        if i % 20 == 0:
            print(f"[{i}/{total}] ...{generated} generated, {skipped} skipped")

    print(f"\n=== Done ===")
    print(f"Total: {total}")
    print(f"Generated SVG: {generated}")
    print(f"Skipped (has JPG): {skipped}")

    # Update dishes.json to reference .svg if no .jpg exists
    updated = 0
    for dish in dishes:
        dish_id = dish["id"]
        jpg_path = os.path.join(IMAGES_DIR, f"{dish_id}.jpg")
        svg_path = os.path.join(IMAGES_DIR, f"{dish_id}.svg")
        if not os.path.exists(jpg_path) and os.path.exists(svg_path):
            dish["image"] = f"images/{dish_id}.svg"
            updated += 1

    if updated:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Updated dishes.json: {updated} dishes now reference SVG images")


if __name__ == "__main__":
    main()
