"""淘宝、天猫 笔记本电脑 评价时间统计"""

import pymongo
import json

client = pymongo.MongoClient("localhost", 27017)
db = client.taobao
collectionItem = db.item
# print(collectionItem.count_documents({}))     # 一共 19069 条商品记录
documents = collectionItem.find({
    '评论数': {'$ne': '暂无评论'},
    "评论详情": {"$exists": True},
})

errInfo = []
dailySalesDic = {'taobao': [], 'tmall': []}
for document in documents:
    arr = dailySalesDic['taobao'] if 'item.taobao.com' in document['带参地址'] else dailySalesDic['tmall']
    commentDetails = document['评论详情']

    i = 0   # 用来查看报错时的条目索引
    for ele in commentDetails:
        details = []
        kDate = ''

        try:
            if 'rateDetail' in ele:
                kDate = 'rateDate'
                details = ele['rateDetail']['rateList']
            elif 'comments' in ele:
                kDate = 'date'
                details = ele['comments']
            else:
                errInfo.append(document['产品ID'] + '     ' + str(i))

            for comment in details:
                if comment[kDate] != '':
                    arr.append(comment[kDate])

        except TypeError:
            errInfo.append(document['产品ID'] + '     ' + str(i))

        i += 1

fileNames = [
    'json/dailySalesTaobao.json',
    'json/dailySalesTmall.json',
    'json/errInfo.json',
]
fileContents = [dailySalesDic['taobao'], dailySalesDic['tmall'], errInfo]
for i in range(len(fileNames)):
    with open(fileNames[i], 'w', encoding='utf-8') as f_obj:
        json.dump(fileContents[i], f_obj, indent=4, ensure_ascii=False)
