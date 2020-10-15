"""小米负面评论词云图可视化"""

import json
from pyecharts import options as opts
from pyecharts.charts import WordCloud

xiaoMiNegativeCommentExtract = []
fileName = 'json/xiaoMiNegativeCommentExtract.json'
with open(fileName, encoding='utf-8') as f_obj:
    xiaoMiNegativeCommentExtract = json.load(f_obj)

data = [(item[0], item[1]) for item in xiaoMiNegativeCommentExtract]

c = (
        WordCloud({'width': '1350px', 'height': '750px'})
        .add("", data, word_size_range=[12, 200], word_gap=0, rotate_step=90)
        .set_global_opts(title_opts=opts.TitleOpts(title="WordCloud-基本示例"))
    ).render('renderHtml/xiaoMiNegativeCommentVisualization.html')
