"""情感分析可视化"""

import json
from pyecharts import options as opts
from pyecharts.charts import Bar

xiaoMiNegativeCommentDic = {}
fileName = 'json/xiaoMiNegativeCommentDic.json'
with open(fileName, encoding='utf-8') as f_obj:
    xiaoMiNegativeCommentDic = json.load(f_obj)

labelsList = list(xiaoMiNegativeCommentDic.keys())
labelsList.sort()
data = [xiaoMiNegativeCommentDic[label] for label in labelsList]

labelsList[0] = '<0.1'
c = (
        Bar()
        .add_xaxis(labelsList)
        .add_yaxis(
            "商家B", data, label_opts=opts.LabelOpts(font_size=16),
        )
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(
                axistick_opts=opts.AxisTickOpts(is_show=False, is_inside=True),
                axislabel_opts=opts.LabelOpts(font_size=16),
            ),
            yaxis_opts=opts.AxisOpts(
                axislabel_opts=opts.LabelOpts(font_size=16),
                axistick_opts=opts.AxisTickOpts(is_inside=True),
            )
        )
    ).render('renderHtml/barSentiment.html')
