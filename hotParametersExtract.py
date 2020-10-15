"""热门参数提取统计"""

import json
import jieba.analyse


def sortExtracts(item):
    return item[1]


featureDescriptions = []
fileName = 'json/featureDescriptions.json'
with open(fileName, encoding='utf-8') as f_obj:
    featureDescriptions = json.load(f_obj)

fileName = 'jieba/stopWords.txt'
jieba.analyse.set_stop_words(fileName)
featureDescriptionsExtract = jieba.analyse.extract_tags(
    '。'.join(featureDescriptions),
    topK=600, withWeight=True
)

featureDescriptionsExtract.sort(key=sortExtracts, reverse=True)

fileName = 'json/featureDescriptionsExtract.json'
with open(fileName, 'w', encoding='utf-8') as f_obj:
    json.dump(featureDescriptionsExtract, f_obj, indent=4, ensure_ascii=False)


