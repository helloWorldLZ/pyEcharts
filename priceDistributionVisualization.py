"""笔记本电脑品价格分布可视化"""

import json
from pyecharts.charts import Pie
from pyecharts import options as opts

priceDistributionDic = {}
fileName = 'json/priceDistribution.json'
with open(fileName, encoding='utf-8') as f_obj:
    priceDistributionDic = json.load(f_obj)

data = [[k, v] for k, v in priceDistributionDic.items()]
txt = '4000 - 6000\n30.11%'
c = (
    Pie()
    # Pie({'width': '1350px', 'height': '750px'})
    .add('', data, radius=["40%", "75%"], label_opts=opts.LabelOpts(formatter="{b}", font_size=16))
    .add('', data, radius=["40%", "75%"], label_opts=opts.LabelOpts(formatter="{d}%", position="inside"))
    .add('', data, radius=["40%", "75%"], label_opts=opts.LabelOpts(formatter=txt, position="center", font_size=22, font_weight='bolder'))
).render('renderHtml/priceDistribution.html')
