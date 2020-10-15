"""小米消极评论观点抽取"""

import pymongo
import json
import baiduAip

client = pymongo.MongoClient("localhost", 27017)
db = client.taobao

miNegComments = []
fileName = 'json/xiaoMiNegativeComment.json'
with open(fileName, encoding='utf-8') as f_obj:
    miNegComments = json.load(f_obj)

start, step = 0, 1
length = len(miNegComments)

print(length)

options = {'type': 13}
nlpClient = baiduAip.getNlpClient()

while True:
    end = start + step
    key = str(start) + '--' + str(end - 1)
    txtList = miNegComments[start:end]
    txt = '。'.join(txtList)
    result = nlpClient.commentTag(txt, options)

    try:
        if 'items' not in result:
            db.tagErr2.insert_many([{
                'index': key,
                'result': result,
                'status': 'notIn',
            }])
        else:
            db.tags2.insert_many([{
                'index': key,
                'result': result['items'],
                'status': 'OK',
            }])

    except Exception:
        db.tagErr2.insert_many([{
            'index': key,
            'result': result,
            'status': 'err'
        }])

    start = end

    if end >= length:
        print(end)
        break
