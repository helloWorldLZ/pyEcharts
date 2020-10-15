"""生成淘宝卖家的经纬度 json 文件"""

import pymongo
import json

client = pymongo.MongoClient("localhost", 27017)
db = client.taobao
collectionItem = db.item
# print(collectionItem.count_documents({}))     # 一共 19069 条商品记录
documents = collectionItem.find({})

myDictionary, shopID, shopPosition = {}, '', []
for document in documents:
    shopID = document['商家ID']
    shopPosition = document['经纬坐标']
    myDictionary[shopID] = shopPosition

# print(len(myDictionary.keys()))     # 一共 2484 家店铺

fileName = 'json/results.json'
with open(fileName, 'w') as f_obj:
    json.dump(myDictionary, f_obj, indent=4)
