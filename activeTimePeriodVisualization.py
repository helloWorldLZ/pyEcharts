"""用户评论活跃时间可视化"""

import json
from pyecharts import options as opts
from pyecharts.charts import Line

dateTimes = []
fileName = 'json/activeTimePeriod.json'
with open(fileName, encoding='utf-8') as f_obj:
    dateTimes = json.load(f_obj)

timePeriodDic = {}
for dateTime in dateTimes:
    dt = dateTime.split()[1]
    key = dt[0:2]

    if key not in timePeriodDic:
        timePeriodDic[key] = 0

    timePeriodDic[key] += 1

labelsList = list(timePeriodDic.keys())
labelsList.sort()
data = [timePeriodDic[label] for label in labelsList]

name = '{:,}'.format(len(dateTimes))
c = (
        Line()
        .add_xaxis(labelsList)
        .add_yaxis(
            "商家B", data, is_symbol_show=False, is_smooth=True,
        )
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(
                axistick_opts=opts.AxisTickOpts(is_inside=True),
                axislabel_opts=opts.LabelOpts(font_size=16),
                boundary_gap=False,
            ),
            yaxis_opts=opts.AxisOpts(
                name='总计 ' + name + ' 人次',
                name_gap=25,
                name_textstyle_opts=opts.TextStyleOpts(font_size=16, font_weight='bold'),
                axislabel_opts=opts.LabelOpts(font_size=16),
                axistick_opts=opts.AxisTickOpts(is_inside=True),
                splitline_opts=opts.SplitLineOpts(is_show=True)
            )
        )
    ).render('renderHtml/activeTimePeriod.html')
