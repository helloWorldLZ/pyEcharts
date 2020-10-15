"""笔记本电脑品牌销量计算"""

import pymongo
import json

client = pymongo.MongoClient("localhost", 27017)
db = client.taobao
collectionItem = db.item
# print(collectionItem.count_documents({}))     # 一共 19069 条商品记录
documents = collectionItem.find({'评论数': {'$ne': '暂无评论'}})

totalCommentsNum = commentsNum = 0
laptopModel = brand = ''
myDictionary = {}
for document in documents:
    tmp = document['评论数']       # 评论数格式为‘xxx条评论’
    commentsNum = int(tmp[0:-3])
    totalCommentsNum += commentsNum

    laptopModel, shopID = document['笔记本型号'], document['商家ID']
    brand = laptopModel.split()[0]

    if brand not in myDictionary.keys():
        myDictionary[brand] = 0

    myDictionary[brand] += commentsNum

fileName = 'json/brandSalesDistribution.json'
with open(fileName, 'w', encoding='utf-8') as f_obj:
    json.dump(myDictionary, f_obj, indent=4, ensure_ascii=False)

# print(totalCommentsNum)     # 一共 929018 条评论
