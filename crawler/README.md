# 中华古典菜肴百科 - 数据爬虫

## 使用方法

```bash
pip install -r requirements.txt
python crawler.py
```

## 功能
- 自动采集200+道经典中华菜肴的详细数据
- 搜索并下载菜肴图片至 `../images/` 目录
- 生成 `../dishes.json` 数据文件

## 输出
- `../dishes.json` — 所有菜肴的结构化数据
- `../images/*.jpg` — 菜肴图片

## 数据来源
- 百度百科
- 美食天下
- 豆果美食

## 字段说明
每个菜肴包含：name, pinyin, cuisine, dynasty, origin, color, aroma, taste, description, story, ingredients, image
