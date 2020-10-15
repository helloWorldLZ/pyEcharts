"""热门参数统计"""

import pymongo
import json

client = pymongo.MongoClient("localhost", 27017)
db = client.taobao
collectionIndex = db.index
documents = collectionIndex.find({})

featureDescriptions = [document['特性描述'] for document in documents]
fileName = 'json/featureDescriptions.json'
with open(fileName, 'w', encoding='utf-8') as f_obj:
    json.dump(featureDescriptions, f_obj, indent=4, ensure_ascii=False)
