"""笔记本电脑日销量可视化"""

import json
from pyecharts import options as opts
from pyecharts.charts import Line

taobaoDic, tmallDic = {}, {}
fileName = 'json/taobaoDic.json'
with open(fileName, encoding='utf-8') as f_obj:
    taobaoDic = json.load(f_obj)

fileName = 'json/tmallDic.json'
with open(fileName, encoding='utf-8') as f_obj:
    tmallDic = json.load(f_obj)

keySet = set(taobaoDic.keys())
keySet.update(tmallDic.keys())

xLabels = list(keySet)
xLabels.sort()

taobaoY, tmallY, totalY = [], [], []
month11Sales = month04Sales = 0
for key in xLabels:
    valueTaobao = taobaoDic[key] if key in taobaoDic.keys() else 0
    valueTmall = tmallDic[key] if key in tmallDic.keys() else 0

    taobaoY.append(valueTaobao)
    tmallY.append(valueTmall)
    totalY.append(valueTaobao + valueTmall)

    if key == '2017年11月15日':
        month11Sales = valueTaobao + valueTmall

    if key == '2018年04月01日':
        month04Sales = valueTaobao + valueTmall

c = (
        Line()
        .add_xaxis(xLabels)
        .add_yaxis(
            "淘宝销量", taobaoY, color='red', is_symbol_show=False,
            linestyle_opts=opts.LineStyleOpts(width=3),
        )
        .add_yaxis(
            "天猫销量", tmallY, color='blue', is_symbol_show=False,
            linestyle_opts=opts.LineStyleOpts(width=3, type_='dashed'),
        )
        .add_yaxis(
            "全网销量", totalY, color='green', is_symbol_show=False,
            linestyle_opts=opts.LineStyleOpts(width=3, type_='dotted'),
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(
                        name='2017年12月12日', value=4602,
                        coord=['2017年12月13日', 4602],
                    ),
                    opts.MarkPointItem(
                        name='2017年11月11日', value=month11Sales,
                        coord=['2017年11月15日', month11Sales],
                    ),
                    opts.MarkPointItem(
                        name='2018年04月01日', value=month04Sales,
                        coord=['2018年04月01日', month04Sales],
                    ),
                ],
                symbol_size=32,
                label_opts=opts.LabelOpts(font_size=12, formatter='{b}\n销量: {c}'),
            ),
        )
        .set_global_opts(
            datazoom_opts=opts.DataZoomOpts(pos_bottom='0'),
            legend_opts=opts.LegendOpts(textstyle_opts=opts.TextStyleOpts(font_size=16)),
            xaxis_opts=opts.AxisOpts(
                axistick_opts=opts.AxisTickOpts(is_inside=True),
                axislabel_opts=opts.LabelOpts(font_size=16),
                boundary_gap=False,
            ),
            yaxis_opts=opts.AxisOpts(
                name='日销量（台）',
                # name_gap=25,
                name_textstyle_opts=opts.TextStyleOpts(font_size=16),
                axislabel_opts=opts.LabelOpts(font_size=16),
                axistick_opts=opts.AxisTickOpts(is_inside=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            )
        )
    ).render('renderHtml/dailySales.html')
