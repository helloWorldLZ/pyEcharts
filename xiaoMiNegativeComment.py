"""小米消极评论抽取"""

import json
from snownlp import SnowNLP

xiaoMiComment = []
fileName = 'json/xiaoMiComment.json'
with open(fileName, encoding='utf-8') as f_obj:
    xiaoMiComment = json.load(f_obj)

xiaoMiNegativeComment = []
xiaoMiNegativeCommentDic = {}
errInfo = []
for comment in xiaoMiComment:
    s = SnowNLP(comment)

    if s.sentiments < 0.3:
        xiaoMiNegativeComment.append(comment)

    sentiKey = str(s.sentiments)
    sentiKey = sentiKey[0:3]

    if sentiKey not in xiaoMiNegativeCommentDic and float(sentiKey) <= 1:
        xiaoMiNegativeCommentDic[sentiKey] = 0

    if float(sentiKey) <= 1:
        xiaoMiNegativeCommentDic[sentiKey] += 1
    else:
        xiaoMiNegativeCommentDic['0.0'] += 1

fileNames = [
    'json/xiaoMiNegativeComment.json',
    'json/xiaoMiNegativeCommentDic.json',
    'json/errInfo.json',
]
fileContents = [xiaoMiNegativeComment, xiaoMiNegativeCommentDic, errInfo]
for i in range(len(fileNames)):
    with open(fileNames[i], 'w', encoding='utf-8') as f_obj:
        json.dump(fileContents[i], f_obj, indent=4, ensure_ascii=False)
