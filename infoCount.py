"""计数"""
import pymongo

client = pymongo.MongoClient("localhost", 27017)
db = client.taobao
collectionItem = db.item

# print(collectionItem.count_documents({}))     # 一共 19069 条商品记录
# print(collectionItem.count_documents({     # 一共 8625 条 有销量商品记录
#     '评论数': {'$ne': '暂无评论'},
#     "评论详情": {"$exists": True},     # 有 10条 错误数据
# }))

documents = collectionItem.find({
    '评论数': {'$ne': '暂无评论'},
    "评论详情": {"$exists": True},     # 有 10条 错误数据
})

totalCommentsNum = 0        # 评论总数
defaultCommentsNum = 0        # 默认评论总数
commentsNum = 0        # 有效评论总数
tianMaoCommentsNum = 0        # 天猫评论总数
soldInDic = {
    'taobao': 0,        # 在淘宝有销量的商品总数
    'tmall': 0        # 在天猫有销量的商品总数
}

for document in documents:
    key = 'taobao' if 'item.taobao.com' in document['带参地址'] else 'tmall'
    soldInDic[key] += 1

    commentDetails = document['评论详情']

    for ele in commentDetails:
        details = []
        keys = []

        try:
            if 'rateDetail' in ele:
                keys = ['rateContent', 'rateDate']
                details = ele['rateDetail']['rateList']
            elif 'comments' in ele:
                keys = ['content', 'date']
                details = ele['comments']

            uselessInfo = [
                '此用户没有填写评论!',
                '此用户没有填写评价。',
                '系统默认评论',
                '15天内买家未作出评价',
                '评价方未及时做出评价,系统默认好评!',
            ]

            totalCommentsNum += len(details)

            if keys[0] == 'rateContent':
                tianMaoCommentsNum += len(details)

            for comment in details:
                if comment[keys[0]] in uselessInfo:
                    defaultCommentsNum += 1
                else:
                    commentsNum += 1

        except TypeError:
            print(document['产品ID'])

print('评论总数:      ', totalCommentsNum)
print('默认评论总数:  ', defaultCommentsNum)
print('有效评论总数:  ', commentsNum)
print('天猫评论总数:  ', tianMaoCommentsNum)
print('有销量的商品总数:  ', soldInDic)
