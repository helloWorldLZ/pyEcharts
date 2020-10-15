"""用户评论、评论时间抽取"""

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

userComments = []
dateTimes = []
errInfo = []
for document in documents:
    commentDetails = document['评论详情']

    i = 0   # 用来查看报错时的条目索引
    for ele in commentDetails:
        details = []
        keys = []
        rateTimeList = []
        rateContentList = []

        try:
            if 'rateDetail' in ele:
                keys = ['rateContent', 'rateDate']
                details = ele['rateDetail']['rateList']
            elif 'comments' in ele:
                keys = ['content', 'date']
                details = ele['comments']
            else:
                errInfo.append(document['产品ID'] + '     ' + str(i))

            uselessInfo = [
                '此用户没有填写评论!',
                '此用户没有填写评价。',
                '系统默认评论',
                '15天内买家未作出评价',
                '评价方未及时做出评价,系统默认好评!',
            ]
            for comment in details:
                if comment[keys[0]] in uselessInfo:
                    continue

                rateContentList.append(comment[keys[0]])
                rateTimeList.append(comment[keys[1]])

        except TypeError:
            errInfo.append(document['产品ID'] + '     ' + str(i))

        userComments.extend(rateContentList)
        dateTimes.extend(rateTimeList)
        i += 1

fileNames = [
    'json/comment.json',
    'json/activeTimePeriod.json',
    'json/errInfo.json',
]
fileContents = [userComments, dateTimes, errInfo]
for i in range(len(fileNames)):
    with open(fileNames[i], 'w', encoding='utf-8') as f_obj:
        json.dump(fileContents[i], f_obj, indent=4, ensure_ascii=False)
