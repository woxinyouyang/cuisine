"""
中华菜肴数据集 - 200+ 经典中国菜式数据库

按菜系分类，涵盖川菜、鲁菜、粤菜、苏菜、浙菜、闽菜、湘菜、徽菜、宫廷菜、民间古典
十大类别，总计 209 道经典菜肴。
"""

DISHES = [
    # ==========================================================================
    # 川菜 (25 dishes)
    # ==========================================================================
    {"name": "宫保鸡丁", "pinyin": "Gōng Bǎo Jī Dīng", "cuisine": "川菜", "dynasty": "清代", "origin": "四川成都"},
    {"name": "麻婆豆腐", "pinyin": "Má Pó Dòu Fǔ", "cuisine": "川菜", "dynasty": "清代", "origin": "四川成都"},
    {"name": "回锅肉", "pinyin": "Huí Guō Ròu", "cuisine": "川菜", "dynasty": "清代", "origin": "四川成都"},
    {"name": "水煮鱼", "pinyin": "Shuǐ Zhǔ Yú", "cuisine": "川菜", "dynasty": "现代", "origin": "四川重庆"},
    {"name": "夫妻肺片", "pinyin": "Fū Qī Fèi Piàn", "cuisine": "川菜", "dynasty": "清代", "origin": "四川成都"},
    {"name": "辣子鸡", "pinyin": "Là Zǐ Jī", "cuisine": "川菜", "dynasty": "清代", "origin": "四川重庆"},
    {"name": "鱼香肉丝", "pinyin": "Yú Xiāng Ròu Sī", "cuisine": "川菜", "dynasty": "民国", "origin": "四川"},
    {"name": "水煮牛肉", "pinyin": "Shuǐ Zhǔ Niú Ròu", "cuisine": "川菜", "dynasty": "宋代", "origin": "四川自贡"},
    {"name": "毛血旺", "pinyin": "Máo Xuè Wàng", "cuisine": "川菜", "dynasty": "民国", "origin": "四川重庆"},
    {"name": "酸菜鱼", "pinyin": "Suān Cài Yú", "cuisine": "川菜", "dynasty": "现代", "origin": "四川重庆"},
    {"name": "水煮肉片", "pinyin": "Shuǐ Zhǔ Ròu Piàn", "cuisine": "川菜", "dynasty": "现代", "origin": "四川"},
    {"name": "担担面", "pinyin": "Dàn Dàn Miàn", "cuisine": "川菜", "dynasty": "清代", "origin": "四川自贡"},
    {"name": "灯影牛肉", "pinyin": "Dēng Yǐng Niú Ròu", "cuisine": "川菜", "dynasty": "清代", "origin": "四川达州"},
    {"name": "口水鸡", "pinyin": "Kǒu Shuǐ Jī", "cuisine": "川菜", "dynasty": "清代", "origin": "四川"},
    {"name": "东坡肘子", "pinyin": "Dōng Pō Zhǒu Zi", "cuisine": "川菜", "dynasty": "宋代", "origin": "四川眉山"},
    {"name": "蒜泥白肉", "pinyin": "Suàn Ní Bái Ròu", "cuisine": "川菜", "dynasty": "清代", "origin": "四川"},
    {"name": "川北凉粉", "pinyin": "Chuān Běi Liáng Fěn", "cuisine": "川菜", "dynasty": "清代", "origin": "四川南充"},
    {"name": "冒菜", "pinyin": "Mào Cài", "cuisine": "川菜", "dynasty": "汉代", "origin": "四川成都"},
    {"name": "干锅", "pinyin": "Gān Guō", "cuisine": "川菜", "dynasty": "现代", "origin": "四川"},
    {"name": "钵钵鸡", "pinyin": "Bō Bō Jī", "cuisine": "川菜", "dynasty": "清代", "origin": "四川乐山"},
    {"name": "老妈蹄花", "pinyin": "Lǎo Mā Tí Huā", "cuisine": "川菜", "dynasty": "清代", "origin": "四川成都"},
    {"name": "宜宾燃面", "pinyin": "Yí Bīn Rán Miàn", "cuisine": "川菜", "dynasty": "清代", "origin": "四川宜宾"},
    {"name": "肥肠粉", "pinyin": "Féi Cháng Fěn", "cuisine": "川菜", "dynasty": "清代", "origin": "四川成都"},
    {"name": "跷脚牛肉", "pinyin": "Qiāo Jiǎo Niú Ròu", "cuisine": "川菜", "dynasty": "清代", "origin": "四川乐山"},
    {"name": "宫保虾仁", "pinyin": "Gōng Bǎo Xiā Rén", "cuisine": "川菜", "dynasty": "清代", "origin": "四川成都"},

    # ==========================================================================
    # 鲁菜 (21 dishes)
    # ==========================================================================
    {"name": "糖醋鲤鱼", "pinyin": "Táng Cù Lǐ Yú", "cuisine": "鲁菜", "dynasty": "唐代", "origin": "山东济南"},
    {"name": "葱烧海参", "pinyin": "Cōng Shāo Hǎi Shēn", "cuisine": "鲁菜", "dynasty": "明代", "origin": "山东烟台"},
    {"name": "九转大肠", "pinyin": "Jiǔ Zhuǎn Dà Cháng", "cuisine": "鲁菜", "dynasty": "清代", "origin": "山东济南"},
    {"name": "油焖大虾", "pinyin": "Yóu Mèn Dà Xiā", "cuisine": "鲁菜", "dynasty": "清代", "origin": "山东"},
    {"name": "德州扒鸡", "pinyin": "Dé Zhōu Pá Jī", "cuisine": "鲁菜", "dynasty": "清代", "origin": "山东德州"},
    {"name": "四喜丸子", "pinyin": "Sì Xǐ Wán Zi", "cuisine": "鲁菜", "dynasty": "唐代", "origin": "山东"},
    {"name": "木须肉", "pinyin": "Mù Xū Ròu", "cuisine": "鲁菜", "dynasty": "清代", "origin": "山东"},
    {"name": "糖醋里脊", "pinyin": "Táng Cù Lǐ Jǐ", "cuisine": "鲁菜", "dynasty": "元代", "origin": "山东"},
    {"name": "锅塌豆腐", "pinyin": "Guō Tā Dòu Fǔ", "cuisine": "鲁菜", "dynasty": "明代", "origin": "山东"},
    {"name": "醋椒鱼", "pinyin": "Cù Jiāo Yú", "cuisine": "鲁菜", "dynasty": "清代", "origin": "山东"},
    {"name": "拔丝山药", "pinyin": "Bá Sī Shān Yào", "cuisine": "鲁菜", "dynasty": "清代", "origin": "山东"},
    {"name": "清汤燕菜", "pinyin": "Qīng Tāng Yàn Cài", "cuisine": "鲁菜", "dynasty": "清代", "origin": "山东济南"},
    {"name": "奶汤蒲菜", "pinyin": "Nǎi Tāng Pú Cài", "cuisine": "鲁菜", "dynasty": "明代", "origin": "山东济南"},
    {"name": "把子肉", "pinyin": "Bǎ Zi Ròu", "cuisine": "鲁菜", "dynasty": "汉代", "origin": "山东济南"},
    {"name": "煎饼卷大葱", "pinyin": "Jiān Bǐng Juǎn Dà Cōng", "cuisine": "鲁菜", "dynasty": "明代", "origin": "山东"},
    {"name": "孔府菜", "pinyin": "Kǒng Fǔ Cài", "cuisine": "鲁菜", "dynasty": "春秋", "origin": "山东曲阜"},
    {"name": "一品豆腐", "pinyin": "Yī Pǐn Dòu Fǔ", "cuisine": "鲁菜", "dynasty": "明代", "origin": "山东"},
    {"name": "坛子肉", "pinyin": "Tán Zi Ròu", "cuisine": "鲁菜", "dynasty": "清代", "origin": "山东济南"},
    {"name": "黄焖鸡", "pinyin": "Huáng Mèn Jī", "cuisine": "鲁菜", "dynasty": "明代", "origin": "山东济南"},
    {"name": "酥锅", "pinyin": "Sū Guō", "cuisine": "鲁菜", "dynasty": "清代", "origin": "山东博山"},
    {"name": "博山豆腐箱", "pinyin": "Bó Shān Dòu Fǔ Xiāng", "cuisine": "鲁菜", "dynasty": "清代", "origin": "山东博山"},

    # ==========================================================================
    # 粤菜 (21 dishes)
    # ==========================================================================
    {"name": "白切鸡", "pinyin": "Bái Qiē Jī", "cuisine": "粤菜", "dynasty": "清代", "origin": "广东广州"},
    {"name": "烤乳猪", "pinyin": "Kǎo Rǔ Zhū", "cuisine": "粤菜", "dynasty": "西周", "origin": "广东"},
    {"name": "龙虎斗", "pinyin": "Lóng Hǔ Dòu", "cuisine": "粤菜", "dynasty": "清代", "origin": "广东广州"},
    {"name": "煲仔饭", "pinyin": "Bāo Zǎi Fàn", "cuisine": "粤菜", "dynasty": "唐代", "origin": "广东广州"},
    {"name": "虾饺", "pinyin": "Xiā Jiǎo", "cuisine": "粤菜", "dynasty": "民国", "origin": "广东广州"},
    {"name": "叉烧", "pinyin": "Chā Shāo", "cuisine": "粤菜", "dynasty": "唐代", "origin": "广东"},
    {"name": "烧鹅", "pinyin": "Shāo É", "cuisine": "粤菜", "dynasty": "宋代", "origin": "广东"},
    {"name": "豉汁蒸排骨", "pinyin": "Chǐ Zhī Zhēng Pái Gǔ", "cuisine": "粤菜", "dynasty": "清代", "origin": "广东"},
    {"name": "白灼虾", "pinyin": "Bái Zhuó Xiā", "cuisine": "粤菜", "dynasty": "清代", "origin": "广东"},
    {"name": "干炒牛河", "pinyin": "Gān Chǎo Niú Hé", "cuisine": "粤菜", "dynasty": "民国", "origin": "广东广州"},
    {"name": "云吞面", "pinyin": "Yún Tūn Miàn", "cuisine": "粤菜", "dynasty": "清代", "origin": "广东广州"},
    {"name": "椰子鸡", "pinyin": "Yē Zi Jī", "cuisine": "粤菜", "dynasty": "汉代", "origin": "海南/广东"},
    {"name": "清蒸鲈鱼", "pinyin": "Qīng Zhēng Lú Yú", "cuisine": "粤菜", "dynasty": "明代", "origin": "广东"},
    {"name": "蜜汁叉烧", "pinyin": "Mì Zhī Chā Shāo", "cuisine": "粤菜", "dynasty": "唐代", "origin": "广东"},
    {"name": "东江盐焗鸡", "pinyin": "Dōng Jiāng Yán Jú Jī", "cuisine": "粤菜", "dynasty": "清代", "origin": "广东东江"},
    {"name": "客家酿豆腐", "pinyin": "Kè Jiā Niàng Dòu Fǔ", "cuisine": "粤菜", "dynasty": "汉代", "origin": "广东客家"},
    {"name": "老火靓汤", "pinyin": "Lǎo Huǒ Liàng Tāng", "cuisine": "粤菜", "dynasty": "宋代", "origin": "广东"},
    {"name": "广式烧肉", "pinyin": "Guǎng Shì Shāo Ròu", "cuisine": "粤菜", "dynasty": "清代", "origin": "广东"},
    {"name": "脆皮烧肉", "pinyin": "Cuì Pí Shāo Ròu", "cuisine": "粤菜", "dynasty": "清代", "origin": "广东"},
    {"name": "姜葱炒蟹", "pinyin": "Jiāng Cōng Chǎo Xiè", "cuisine": "粤菜", "dynasty": "明代", "origin": "广东"},
    {"name": "肠粉", "pinyin": "Cháng Fěn", "cuisine": "粤菜", "dynasty": "清代", "origin": "广东广州"},

    # ==========================================================================
    # 苏菜 (21 dishes)
    # ==========================================================================
    {"name": "松鼠鳜鱼", "pinyin": "Sōng Shǔ Guì Yú", "cuisine": "苏菜", "dynasty": "清代", "origin": "江苏苏州"},
    {"name": "叫花鸡", "pinyin": "Jiào Huā Jī", "cuisine": "苏菜", "dynasty": "清代", "origin": "江苏常熟"},
    {"name": "狮子头", "pinyin": "Shī Zi Tóu", "cuisine": "苏菜", "dynasty": "隋代", "origin": "江苏扬州"},
    {"name": "大煮干丝", "pinyin": "Dà Zhǔ Gān Sī", "cuisine": "苏菜", "dynasty": "清代", "origin": "江苏扬州"},
    {"name": "盐水鸭", "pinyin": "Yán Shuǐ Yā", "cuisine": "苏菜", "dynasty": "宋代", "origin": "江苏南京"},
    {"name": "清炖蟹粉狮子头", "pinyin": "Qīng Dùn Xiè Fěn Shī Zi Tóu", "cuisine": "苏菜", "dynasty": "隋代", "origin": "江苏扬州"},
    {"name": "无锡排骨", "pinyin": "Wú Xī Pái Gǔ", "cuisine": "苏菜", "dynasty": "清代", "origin": "江苏无锡"},
    {"name": "水晶肴肉", "pinyin": "Shuǐ Jīng Yáo Ròu", "cuisine": "苏菜", "dynasty": "清代", "origin": "江苏镇江"},
    {"name": "碧螺虾仁", "pinyin": "Bì Luó Xiā Rén", "cuisine": "苏菜", "dynasty": "清代", "origin": "江苏苏州"},
    {"name": "莼菜银鱼汤", "pinyin": "Chún Cài Yín Yú Tāng", "cuisine": "苏菜", "dynasty": "晋代", "origin": "江苏太湖"},
    {"name": "蟹粉豆腐", "pinyin": "Xiè Fěn Dòu Fǔ", "cuisine": "苏菜", "dynasty": "清代", "origin": "江苏"},
    {"name": "枫镇大面", "pinyin": "Fēng Zhèn Dà Miàn", "cuisine": "苏菜", "dynasty": "清代", "origin": "江苏苏州"},
    {"name": "常州糟扣肉", "pinyin": "Cháng Zhōu Zāo Kòu Ròu", "cuisine": "苏菜", "dynasty": "清代", "origin": "江苏常州"},
    {"name": "沛县狗肉", "pinyin": "Pèi Xiàn Gǒu Ròu", "cuisine": "苏菜", "dynasty": "汉代", "origin": "江苏沛县"},
    {"name": "扬州炒饭", "pinyin": "Yáng Zhōu Chǎo Fàn", "cuisine": "苏菜", "dynasty": "清代", "origin": "江苏扬州"},
    {"name": "南京板鸭", "pinyin": "Nán Jīng Bǎn Yā", "cuisine": "苏菜", "dynasty": "明代", "origin": "江苏南京"},
    {"name": "酱排骨", "pinyin": "Jiàng Pái Gǔ", "cuisine": "苏菜", "dynasty": "清代", "origin": "江苏无锡"},
    {"name": "淮安软兜", "pinyin": "Huái ān Ruǎn Dōu", "cuisine": "苏菜", "dynasty": "清代", "origin": "江苏淮安"},
    {"name": "平桥豆腐", "pinyin": "Píng Qiáo Dòu Fǔ", "cuisine": "苏菜", "dynasty": "清代", "origin": "江苏淮安"},
    {"name": "文思豆腐", "pinyin": "Wén Sī Dòu Fǔ", "cuisine": "苏菜", "dynasty": "清代", "origin": "江苏扬州"},
    {"name": "三套鸭", "pinyin": "Sān Tào Yā", "cuisine": "苏菜", "dynasty": "清代", "origin": "江苏扬州"},

    # ==========================================================================
    # 浙菜 (21 dishes)
    # ==========================================================================
    {"name": "东坡肉", "pinyin": "Dōng Pō Ròu", "cuisine": "浙菜", "dynasty": "宋代", "origin": "浙江杭州"},
    {"name": "西湖醋鱼", "pinyin": "Xī Hú Cù Yú", "cuisine": "浙菜", "dynasty": "宋代", "origin": "浙江杭州"},
    {"name": "龙井虾仁", "pinyin": "Lóng Jǐng Xiā Rén", "cuisine": "浙菜", "dynasty": "清代", "origin": "浙江杭州"},
    {"name": "绍兴醉鸡", "pinyin": "Shào Xīng Zuì Jī", "cuisine": "浙菜", "dynasty": "明代", "origin": "浙江绍兴"},
    {"name": "荷叶粉蒸肉", "pinyin": "Hé Yè Fěn Zhēng Ròu", "cuisine": "浙菜", "dynasty": "清代", "origin": "浙江"},
    {"name": "宋嫂鱼羹", "pinyin": "Sòng Sǎo Yú Gēng", "cuisine": "浙菜", "dynasty": "宋代", "origin": "浙江杭州"},
    {"name": "干炸响铃", "pinyin": "Gàn Zhà Xiǎng Líng", "cuisine": "浙菜", "dynasty": "清代", "origin": "浙江杭州"},
    {"name": "叫化童鸡", "pinyin": "Jiào Huà Tóng Jī", "cuisine": "浙菜", "dynasty": "清代", "origin": "浙江杭州"},
    {"name": "冰糖甲鱼", "pinyin": "Bīng Táng Jiǎ Yú", "cuisine": "浙菜", "dynasty": "清代", "origin": "浙江宁波"},
    {"name": "宁波汤圆", "pinyin": "Níng Bō Tāng Yuán", "cuisine": "浙菜", "dynasty": "宋代", "origin": "浙江宁波"},
    {"name": "西湖莼菜汤", "pinyin": "Xī Hú Chún Cài Tāng", "cuisine": "浙菜", "dynasty": "晋代", "origin": "浙江杭州"},
    {"name": "雪菜大汤黄鱼", "pinyin": "Xuě Cài Dà Tāng Huáng Yú", "cuisine": "浙菜", "dynasty": "清代", "origin": "浙江宁波"},
    {"name": "金华火腿", "pinyin": "Jīn Huá Huǒ Tuǐ", "cuisine": "浙菜", "dynasty": "唐代", "origin": "浙江金华"},
    {"name": "温州鱼丸", "pinyin": "Wēn Zhōu Yú Wán", "cuisine": "浙菜", "dynasty": "明代", "origin": "浙江温州"},
    {"name": "嘉兴粽子", "pinyin": "Jiā Xīng Zòng Zi", "cuisine": "浙菜", "dynasty": "明代", "origin": "浙江嘉兴"},
    {"name": "蛤蜊黄鱼羹", "pinyin": "Gé Lí Huáng Yú Gēng", "cuisine": "浙菜", "dynasty": "清代", "origin": "浙江宁波"},
    {"name": "油焖笋", "pinyin": "Yóu Mèn Sǔn", "cuisine": "浙菜", "dynasty": "清代", "origin": "浙江杭州"},
    {"name": "梅干菜扣肉", "pinyin": "Méi Gān Cài Kòu Ròu", "cuisine": "浙菜", "dynasty": "明代", "origin": "浙江绍兴"},
    {"name": "糟溜鱼片", "pinyin": "Zāo Liū Yú Piàn", "cuisine": "浙菜", "dynasty": "清代", "origin": "浙江"},
    {"name": "八宝菜", "pinyin": "Bā Bǎo Cài", "cuisine": "浙菜", "dynasty": "清代", "origin": "浙江杭州"},
    {"name": "咸菜大汤黄鱼", "pinyin": "Xián Cài Dà Tāng Huáng Yú", "cuisine": "浙菜", "dynasty": "清代", "origin": "浙江宁波"},

    # ==========================================================================
    # 闽菜 (16 dishes)
    # ==========================================================================
    {"name": "佛跳墙", "pinyin": "Fó Tiào Qiáng", "cuisine": "闽菜", "dynasty": "清代", "origin": "福建福州"},
    {"name": "荔枝肉", "pinyin": "Lì Zhī Ròu", "cuisine": "闽菜", "dynasty": "清代", "origin": "福建福州"},
    {"name": "沙茶面", "pinyin": "Shā Chá Miàn", "cuisine": "闽菜", "dynasty": "民国", "origin": "福建厦门"},
    {"name": "海蛎煎", "pinyin": "Hǎi Lì Jiān", "cuisine": "闽菜", "dynasty": "明代", "origin": "福建厦门"},
    {"name": "闽生果", "pinyin": "Mǐn Shēng Guǒ", "cuisine": "闽菜", "dynasty": "清代", "origin": "福建"},
    {"name": "福州鱼丸", "pinyin": "Fú Zhōu Yú Wán", "cuisine": "闽菜", "dynasty": "明代", "origin": "福建福州"},
    {"name": "佛手排骨", "pinyin": "Fó Shǒu Pái Gǔ", "cuisine": "闽菜", "dynasty": "清代", "origin": "福建泉州"},
    {"name": "炒西施舌", "pinyin": "Chǎo Xī Shī Shé", "cuisine": "闽菜", "dynasty": "清代", "origin": "福建"},
    {"name": "太极大银丝", "pinyin": "Tài Jí Dà Yín Sī", "cuisine": "闽菜", "dynasty": "清代", "origin": "福建"},
    {"name": "鸡汤汆海蚌", "pinyin": "Jī Tāng Cuān Hǎi Bàng", "cuisine": "闽菜", "dynasty": "清代", "origin": "福建福州"},
    {"name": "淡糟香螺片", "pinyin": "Dàn Zāo Xiāng Luó Piàn", "cuisine": "闽菜", "dynasty": "清代", "origin": "福建福州"},
    {"name": "土笋冻", "pinyin": "Tǔ Sǔn Dòng", "cuisine": "闽菜", "dynasty": "明代", "origin": "福建泉州"},
    {"name": "闽南醋肉", "pinyin": "Mǐn Nán Cù Ròu", "cuisine": "闽菜", "dynasty": "宋代", "origin": "福建泉州"},
    {"name": "面线糊", "pinyin": "Miàn Xiàn Hú", "cuisine": "闽菜", "dynasty": "清代", "origin": "福建泉州"},
    {"name": "同安封肉", "pinyin": "Tóng ān Fēng Ròu", "cuisine": "闽菜", "dynasty": "清代", "origin": "福建同安"},
    {"name": "半月沉江", "pinyin": "Bàn Yuè Chén Jiāng", "cuisine": "闽菜", "dynasty": "唐代", "origin": "福建厦门"},

    # ==========================================================================
    # 湘菜 (16 dishes)
    # ==========================================================================
    {"name": "剁椒鱼头", "pinyin": "Duò Jiāo Yú Tóu", "cuisine": "湘菜", "dynasty": "清代", "origin": "湖南长沙"},
    {"name": "毛氏红烧肉", "pinyin": "Máo Shì Hóng Shāo Ròu", "cuisine": "湘菜", "dynasty": "现代", "origin": "湖南湘潭"},
    {"name": "臭豆腐", "pinyin": "Chòu Dòu Fǔ", "cuisine": "湘菜", "dynasty": "清代", "origin": "湖南长沙"},
    {"name": "湘西外婆菜", "pinyin": "Xiāng Xī Wài Pó Cài", "cuisine": "湘菜", "dynasty": "清代", "origin": "湖南湘西"},
    {"name": "腊味合蒸", "pinyin": "Là Wèi Hé Zhēng", "cuisine": "湘菜", "dynasty": "汉代", "origin": "湖南"},
    {"name": "东安子鸡", "pinyin": "Dōng ān Zǐ Jī", "cuisine": "湘菜", "dynasty": "唐代", "origin": "湖南东安"},
    {"name": "辣椒炒肉", "pinyin": "Là Jiāo Chǎo Ròu", "cuisine": "湘菜", "dynasty": "清代", "origin": "湖南"},
    {"name": "口味虾", "pinyin": "Kǒu Wèi Xiā", "cuisine": "湘菜", "dynasty": "现代", "origin": "湖南长沙"},
    {"name": "湖南米粉", "pinyin": "Hú Nán Mǐ Fěn", "cuisine": "湘菜", "dynasty": "清代", "origin": "湖南"},
    {"name": "湘味蒸菜", "pinyin": "Xiāng Wèi Zhēng Cài", "cuisine": "湘菜", "dynasty": "明代", "origin": "湖南"},
    {"name": "永州血鸭", "pinyin": "Yǒng Zhōu Xuè Yā", "cuisine": "湘菜", "dynasty": "清代", "origin": "湖南永州"},
    {"name": "麻仁酥鸡", "pinyin": "Má Rén Sū Jī", "cuisine": "湘菜", "dynasty": "清代", "origin": "湖南"},
    {"name": "洞庭湖藕汤", "pinyin": "Dòng Tíng Hú Ǒu Tāng", "cuisine": "湘菜", "dynasty": "宋代", "origin": "湖南洞庭湖"},
    {"name": "酸辣粉", "pinyin": "Suān Là Fěn", "cuisine": "湘菜", "dynasty": "清代", "origin": "湖南"},
    {"name": "湘西腊肉", "pinyin": "Xiāng Xī Là Ròu", "cuisine": "湘菜", "dynasty": "明代", "origin": "湖南湘西"},
    {"name": "浏阳蒸菜", "pinyin": "Liú Yáng Zhēng Cài", "cuisine": "湘菜", "dynasty": "明代", "origin": "湖南浏阳"},

    # ==========================================================================
    # 徽菜 (16 dishes)
    # ==========================================================================
    {"name": "臭鳜鱼", "pinyin": "Chòu Guì Yú", "cuisine": "徽菜", "dynasty": "清代", "origin": "安徽黄山"},
    {"name": "毛豆腐", "pinyin": "Máo Dòu Fǔ", "cuisine": "徽菜", "dynasty": "明代", "origin": "安徽黄山"},
    {"name": "一品锅", "pinyin": "Yī Pǐn Guō", "cuisine": "徽菜", "dynasty": "清代", "origin": "安徽绩溪"},
    {"name": "黄山炖鸽", "pinyin": "Huáng Shān Dùn Gē", "cuisine": "徽菜", "dynasty": "清代", "origin": "安徽黄山"},
    {"name": "徽州蒸鸡", "pinyin": "Huī Zhōu Zhēng Jī", "cuisine": "徽菜", "dynasty": "明代", "origin": "安徽徽州"},
    {"name": "问政山笋", "pinyin": "Wèn Zhèng Shān Sǔn", "cuisine": "徽菜", "dynasty": "明代", "origin": "安徽歙县"},
    {"name": "胡氏一品锅", "pinyin": "Hú Shì Yī Pǐn Guō", "cuisine": "徽菜", "dynasty": "清代", "origin": "安徽绩溪"},
    {"name": "方腊鱼", "pinyin": "Fāng Là Yú", "cuisine": "徽菜", "dynasty": "宋代", "origin": "安徽"},
    {"name": "中和汤", "pinyin": "Zhōng Hé Tāng", "cuisine": "徽菜", "dynasty": "清代", "origin": "安徽"},
    {"name": "无为熏鸭", "pinyin": "Wú Wéi Xūn Yā", "cuisine": "徽菜", "dynasty": "清代", "origin": "安徽无为"},
    {"name": "李鸿章杂烩", "pinyin": "Lǐ Hōng Zhāng Zá Huì", "cuisine": "徽菜", "dynasty": "清代", "origin": "安徽合肥"},
    {"name": "淮南牛肉汤", "pinyin": "Huái Nán Niú Ròu Tāng", "cuisine": "徽菜", "dynasty": "汉代", "origin": "安徽淮南"},
    {"name": "葡萄鱼", "pinyin": "Pú Tao Yú", "cuisine": "徽菜", "dynasty": "清代", "origin": "安徽"},
    {"name": "绩溪炒粉丝", "pinyin": "Jì Xī Chǎo Fěn Sī", "cuisine": "徽菜", "dynasty": "明代", "origin": "安徽绩溪"},
    {"name": "徽州刀板香", "pinyin": "Huī Zhōu Dāo Bǎn Xiāng", "cuisine": "徽菜", "dynasty": "明代", "origin": "安徽徽州"},
    {"name": "云雾肉", "pinyin": "Yún Wù Ròu", "cuisine": "徽菜", "dynasty": "清代", "origin": "安徽"},

    # ==========================================================================
    # 宫廷菜 (20 dishes)
    # ==========================================================================
    {"name": "北京烤鸭", "pinyin": "Běi Jīng Kǎo Yā", "cuisine": "宫廷菜", "dynasty": "明代", "origin": "北京"},
    {"name": "涮羊肉", "pinyin": "Shuàn Yáng Ròu", "cuisine": "宫廷菜", "dynasty": "元代", "origin": "北京"},
    {"name": "驴打滚", "pinyin": "Lǘ Dǎ Gǔn", "cuisine": "宫廷菜", "dynasty": "清代", "origin": "北京"},
    {"name": "豌豆黄", "pinyin": "Wān Dòu Huáng", "cuisine": "宫廷菜", "dynasty": "清代", "origin": "北京"},
    {"name": "芸豆卷", "pinyin": "Yún Dòu Juǎn", "cuisine": "宫廷菜", "dynasty": "清代", "origin": "北京"},
    {"name": "艾窝窝", "pinyin": "Ài Wō Wō", "cuisine": "宫廷菜", "dynasty": "明代", "origin": "北京"},
    {"name": "肉末烧饼", "pinyin": "Ròu Mò Shāo Bǐng", "cuisine": "宫廷菜", "dynasty": "清代", "origin": "北京"},
    {"name": "宫廷奶酪", "pinyin": "Gōng Tíng Nǎi Lào", "cuisine": "宫廷菜", "dynasty": "清代", "origin": "北京"},
    {"name": "蜜供", "pinyin": "Mì Gòng", "cuisine": "宫廷菜", "dynasty": "清代", "origin": "北京"},
    {"name": "抓炒里脊", "pinyin": "Zhuā Chǎo Lǐ Jǐ", "cuisine": "宫廷菜", "dynasty": "清代", "origin": "北京"},
    {"name": "红娘自配", "pinyin": "Hóng Niáng Zì Pèi", "cuisine": "宫廷菜", "dynasty": "清代", "origin": "北京"},
    {"name": "宫保野兔", "pinyin": "Gōng Bǎo Yě Tù", "cuisine": "宫廷菜", "dynasty": "清代", "origin": "北京"},
    {"name": "八宝鸭", "pinyin": "Bā Bǎo Yā", "cuisine": "宫廷菜", "dynasty": "清代", "origin": "北京"},
    {"name": "菊花佛手", "pinyin": "Jú Huā Fó Shǒu", "cuisine": "宫廷菜", "dynasty": "清代", "origin": "北京"},
    {"name": "糖火烧", "pinyin": "Táng Huǒ Shāo", "cuisine": "宫廷菜", "dynasty": "明代", "origin": "北京"},
    {"name": "萨琪玛", "pinyin": "Sà Qí Mǎ", "cuisine": "宫廷菜", "dynasty": "清代", "origin": "北京"},
    {"name": "全鱼宴", "pinyin": "Quán Yú Yàn", "cuisine": "宫廷菜", "dynasty": "清代", "origin": "河北白洋淀"},
    {"name": "满汉全席", "pinyin": "Mǎn Hàn Quán Xí", "cuisine": "宫廷菜", "dynasty": "清代", "origin": "北京"},
    {"name": "元宝肉", "pinyin": "Yuán Bǎo Ròu", "cuisine": "宫廷菜", "dynasty": "清代", "origin": "北京"},
    {"name": "翡翠白玉汤", "pinyin": "Fěi Cuì Bái Yù Tāng", "cuisine": "宫廷菜", "dynasty": "明代", "origin": "北京"},

    # ==========================================================================
    # 民间古典 (32 dishes)
    # ==========================================================================
    {"name": "粽子", "pinyin": "Zòng Zi", "cuisine": "民间古典", "dynasty": "战国", "origin": "全国"},
    {"name": "月饼", "pinyin": "Yuè Bǐng", "cuisine": "民间古典", "dynasty": "唐代", "origin": "全国"},
    {"name": "腊八粥", "pinyin": "Là Bā Zhōu", "cuisine": "民间古典", "dynasty": "宋代", "origin": "全国"},
    {"name": "豆腐脑", "pinyin": "Dòu Fǔ Nǎo", "cuisine": "民间古典", "dynasty": "汉代", "origin": "全国"},
    {"name": "春卷", "pinyin": "Chūn Juǎn", "cuisine": "民间古典", "dynasty": "唐代", "origin": "全国"},
    {"name": "年糕", "pinyin": "Nián Gāo", "cuisine": "民间古典", "dynasty": "汉代", "origin": "全国"},
    {"name": "汤圆", "pinyin": "Tāng Yuán", "cuisine": "民间古典", "dynasty": "宋代", "origin": "全国"},
    {"name": "饺子", "pinyin": "Jiǎo Zi", "cuisine": "民间古典", "dynasty": "汉代", "origin": "全国"},
    {"name": "油条", "pinyin": "Yóu Tiáo", "cuisine": "民间古典", "dynasty": "宋代", "origin": "全国"},
    {"name": "豆浆", "pinyin": "Dòu Jiāng", "cuisine": "民间古典", "dynasty": "汉代", "origin": "全国"},
    {"name": "凉皮", "pinyin": "Liáng Pí", "cuisine": "民间古典", "dynasty": "唐代", "origin": "陕西"},
    {"name": "肉夹馍", "pinyin": "Ròu Jiā Mó", "cuisine": "民间古典", "dynasty": "战国", "origin": "陕西"},
    {"name": "羊肉泡馍", "pinyin": "Yáng Ròu Pào Mó", "cuisine": "民间古典", "dynasty": "宋代", "origin": "陕西西安"},
    {"name": "胡辣汤", "pinyin": "Hú Là Tāng", "cuisine": "民间古典", "dynasty": "明代", "origin": "河南"},
    {"name": "煎饼果子", "pinyin": "Jiān Bǐng Guǒ Zi", "cuisine": "民间古典", "dynasty": "明代", "origin": "天津"},
    {"name": "刀削面", "pinyin": "Dāo Xuē Miàn", "cuisine": "民间古典", "dynasty": "元代", "origin": "山西"},
    {"name": "兰州牛肉面", "pinyin": "Lán Zhōu Niú Ròu Miàn", "cuisine": "民间古典", "dynasty": "清代", "origin": "甘肃兰州"},
    {"name": "过桥米线", "pinyin": "Guò Qiáo Mǐ Xiàn", "cuisine": "民间古典", "dynasty": "清代", "origin": "云南"},
    {"name": "小笼包", "pinyin": "Xiǎo Lóng Bāo", "cuisine": "民间古典", "dynasty": "清代", "origin": "上海/江苏"},
    {"name": "生煎包", "pinyin": "Shēng Jiān Bāo", "cuisine": "民间古典", "dynasty": "民国", "origin": "上海"},
    {"name": "灌汤包", "pinyin": "Guàn Tāng Bāo", "cuisine": "民间古典", "dynasty": "宋代", "origin": "河南开封"},
    {"name": "冰糖葫芦", "pinyin": "Bīng Táng Hú Lu", "cuisine": "民间古典", "dynasty": "宋代", "origin": "北京"},
    {"name": "烧麦", "pinyin": "Shāo Mài", "cuisine": "民间古典", "dynasty": "明代", "origin": "北京"},
    {"name": "豆汁", "pinyin": "Dòu Zhī", "cuisine": "民间古典", "dynasty": "清代", "origin": "北京"},
    {"name": "桂花糕", "pinyin": "Guì Huā Gāo", "cuisine": "民间古典", "dynasty": "明代", "origin": "全国"},
    {"name": "糍粑", "pinyin": "Cí Bā", "cuisine": "民间古典", "dynasty": "战国", "origin": "湖南/湖北"},
    {"name": "锅贴", "pinyin": "Guō Tiē", "cuisine": "民间古典", "dynasty": "宋代", "origin": "全国"},
    {"name": "馄饨", "pinyin": "Hún Tun", "cuisine": "民间古典", "dynasty": "汉代", "origin": "全国"},
    {"name": "烧饼", "pinyin": "Shāo Bǐng", "cuisine": "民间古典", "dynasty": "汉代", "origin": "全国"},
    {"name": "炸酱面", "pinyin": "Zhà Jiàng Miàn", "cuisine": "民间古典", "dynasty": "清代", "origin": "北京"},
    {"name": "酸梅汤", "pinyin": "Suān Méi Tāng", "cuisine": "民间古典", "dynasty": "清代", "origin": "北京"},
    {"name": "豆腐", "pinyin": "Dòu Fǔ", "cuisine": "民间古典", "dynasty": "汉代", "origin": "全国"},
]


def get_cuisine_groups():
    """按菜系分组，返回 dict[菜系名, list[菜肴dict]]"""
    groups = {}
    for dish in DISHES:
        cuisine = dish["cuisine"]
        if cuisine not in groups:
            groups[cuisine] = []
        groups[cuisine].append(dish)
    return groups


def get_dynasty_groups():
    """按朝代分组，返回 dict[朝代名, list[菜肴dict]]"""
    groups = {}
    for dish in DISHES:
        dynasty = dish["dynasty"]
        if dynasty not in groups:
            groups[dynasty] = []
        groups[dynasty].append(dish)
    return groups


# =============================================================================
# 自检：当模块被直接运行时打印统计信息
# =============================================================================
if __name__ == "__main__":
    total = len(DISHES)
    cuisine_groups = get_cuisine_groups()
    dynasty_groups = get_dynasty_groups()

    print(f"菜肴总数: {total}")
    print()
    print("--- 按菜系 ---")
    for cuisine, dishes in sorted(cuisine_groups.items()):
        print(f"  {cuisine}: {len(dishes)} 道")
    print()
    print("--- 按朝代 ---")
    for dynasty, dishes in sorted(dynasty_groups.items()):
        print(f"  {dynasty}: {len(dishes)} 道")
