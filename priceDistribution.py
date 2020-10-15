"""笔记本电脑价格统计"""

import pymongo
import json

client = pymongo.MongoClient("localhost", 27017)
db = client.taobao
collectionItem = db.item
# print(collectionItem.count_documents({}))     # 一共 19069 条商品记录
documents = collectionItem.find({})

priceDistributionDic = {
    '0-2000': 0,
    '2000-4000': 0,
    '4000-6000': 0,
    '6000-8000': 0,
    '8000-10000': 0,
    '10000-12000': 0,
    '12000-14000': 0,
    # '14000-16000': 0,
    '>12000': 0
}

for document in documents:
    price = float(document['价格'])

    if price < 2000:
        priceDistributionDic['0-2000'] += 1
    elif price < 4000:
        priceDistributionDic['2000-4000'] += 1
    elif price < 6000:
        priceDistributionDic['4000-6000'] += 1
    elif price < 8000:
        priceDistributionDic['6000-8000'] += 1
    elif price < 10000:
        priceDistributionDic['8000-10000'] += 1
    elif price < 12000:
        priceDistributionDic['10000-12000'] += 1
    elif price < 14000:
        priceDistributionDic['12000-14000'] += 1
    # elif price < 16000:
    #     priceDistributionDic['14000-16000'] += 1
    else:
        priceDistributionDic['>12000'] += 1

fileName = 'json/priceDistribution.json'
with open(fileName, 'w', encoding='utf-8') as f_obj:
    json.dump(priceDistributionDic, f_obj, indent=4, ensure_ascii=False)
