"""笔记本电脑品牌销量可视化"""

import json
from pyecharts import options as opts
from pyecharts.charts import TreeMap

brandSalesDic = {}
fileName = 'json/brandSalesDistribution.json'
with open(fileName, encoding='utf-8') as f_obj:
    brandSalesDic = json.load(f_obj)

data = []
otherBrands = 0     # 用于其它品牌笔记本电脑的统计
for kBrand, vSales in brandSalesDic.items():
    if vSales < 5000:
        otherBrands += vSales
    else:
        data.append({
            'value': vSales,
            'name': kBrand + '\n' + '{:.2%}'.format(vSales/929018)
        })

data.append({
    'value': otherBrands,
    'name': '其它品牌\n' + '{:.2%}'.format(otherBrands/929018)
})
c = (
        TreeMap({'width': '1300px', 'height': '800px'})
        .add("演示数据", data, label_opts=opts.LabelOpts(position='inside', vertical_align='middle', font_size=18, font_weight='bolder'))
        .set_global_opts(legend_opts=opts.LegendOpts(is_show=False))
    ).render('renderHtml/brandSales.html')
