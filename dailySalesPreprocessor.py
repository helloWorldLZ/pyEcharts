"""笔记本电脑日销量数据预处理"""

import json

dailySalesTaobao, taobaoDic = [], {}
fileName = 'json/dailySalesTaobao.json'
with open(fileName, encoding='utf-8') as f_obj:
    dailySalesTaobao = json.load(f_obj)     # 219836 条

for dateTime in dailySalesTaobao:
    dtKey = dateTime.split()[0]

    if dtKey not in taobaoDic:
        taobaoDic[dtKey] = 0

    taobaoDic[dtKey] += 1

dailySalesTmall, tmallDic = [], {}
fileName = 'json/dailySalesTmall.json'
with open(fileName, encoding='utf-8') as f_obj:
    dailySalesTmall = json.load(f_obj)      # 351997 条

for dateTime in dailySalesTmall:
    dtKey = dateTime.split()[0]
    dtKey = dtKey.replace('-', '年', 1)
    dtKey = dtKey.replace('-', '月') + '日'

    if dtKey not in tmallDic:
        tmallDic[dtKey] = 0

    tmallDic[dtKey] += 1

fileNames = [
    'json/taobaoDic.json',
    'json/tmallDic.json',
]
fileContents = [taobaoDic, tmallDic]
for i in range(len(fileNames)):
    with open(fileNames[i], 'w', encoding='utf-8') as f_obj:
        json.dump(fileContents[i], f_obj, indent=4, ensure_ascii=False)

# 571833 条
print(
    len(dailySalesTaobao), len(dailySalesTmall),
    len(dailySalesTmall) + len(dailySalesTaobao)
)
