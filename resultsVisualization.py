"""对淘宝卖家的经纬度位置进行可视化"""

import json
from pyecharts.charts import Geo
from pyecharts import options as opts

fileName = 'json/results.json'
with open(fileName) as f_obj:
    myDictionary = json.load(f_obj)


def geo_base() -> Geo:
    c = (
        Geo()
        .add_schema(maptype="world")
        .add_coordinate_json(fileName)
        .add('', [[key, 0] for key in myDictionary.keys()], symbol_size=10)
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    )
    return c


geo_base().render('renderHtml/world.html')
