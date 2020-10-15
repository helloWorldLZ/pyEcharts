"""笔记本电脑品牌商家占有量计算"""

import pymongo
import json

client = pymongo.MongoClient("localhost", 27017)
db = client.taobao
collectionItem = db.item
# print(collectionItem.count_documents({}))     # 一共 19069 条商品记录
documents = collectionItem.find({})

laptopModel = brand = shopID = ''
# brandSet = set()
myDictionary = {}
for document in documents:
    laptopModel, shopID = document['笔记本型号'], document['商家ID']
    brand = laptopModel.split()[0]

    if brand not in myDictionary.keys():
        myDictionary[brand] = []

    if shopID not in myDictionary[brand]:
        myDictionary[brand].append(shopID)

brandTotalShoppersDic = {}
for kBrand, vShoppers in myDictionary.items():
    brandTotalShoppersDic[kBrand] = len(vShoppers)

fileName = 'json/brandTotalShoppers.json'
with open(fileName, 'w', encoding='utf-8') as f_obj:
    json.dump(brandTotalShoppersDic, f_obj, indent=4, ensure_ascii=False)

# fileName = 'json/brandDistribution.json'
# with open(fileName, 'w', encoding='utf-8') as f_obj:
#     json.dump(myDictionary, f_obj, indent=4, ensure_ascii=False)

# fileName = 'json/brandSet.json'
# with open(fileName, 'w', encoding='utf-8') as f_obj:
#     json.dump(list(brandSet), f_obj, ensure_ascii=False, indent=4)
