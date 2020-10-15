"""小米负面评论词云图, 这个文件没用"""

import pymongo
from wordcloud import WordCloud
import matplotlib.pyplot as plt

client = pymongo.MongoClient("localhost", 27017)
db = client.taobao
tagsCollection = db.tags
documents = tagsCollection.find({})

txt = ''
txts = []
for document in documents:
    for res in document['result']:
        if res['sentiment'] == 2:
            continue

        txt += res['prop'] + res['adj'] + '。'

# lower max_font_size
font = "msyh.ttc"
wordcloud = WordCloud(
    font_path=font,
    collocations=False,
    background_color='white',
    max_font_size=260,
    max_words=2000,
    stopwords={'鼠标一般', '电脑一般'},
    width=1600,
    height=900
).generate(txt)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
