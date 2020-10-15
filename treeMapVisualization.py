"""笔记本电脑品牌商家占有量可视化"""

import json
from pyecharts import options as opts
from pyecharts.charts import TreeMap

brandTotalShoppersDic = {}
fileName = 'json/brandTotalShoppers.json'
with open(fileName, encoding='utf-8') as f_obj:
    brandTotalShoppersDic = json.load(f_obj)

# 这块代码后来加上的，懒得改结构了
denominator = 0
for kBrand, vShoppers in brandTotalShoppersDic.items():
    denominator += vShoppers

data = []
otherBrands = 0     # 用于其它品牌笔记本电脑的统计
for kBrand, vShoppers in brandTotalShoppersDic.items():
    if vShoppers < 19:
        otherBrands += 1
    else:
        data.append({
            'value': vShoppers,
            'name': kBrand + '\n' + '{:.2%}'.format(vShoppers/denominator)
        })

data.append({
    'value': otherBrands,
    'name': '其它品牌\n' + '{:.2%}'.format(otherBrands/denominator)
})
c = (
        TreeMap({'width': '1500px', 'height': '1000px'})
        .add("演示数据", data, label_opts=opts.LabelOpts(position='inside', vertical_align='middle', font_size=18, font_weight='bolder'))
        .set_global_opts(legend_opts=opts.LegendOpts(is_show=False))
    ).render('renderHtml/brandTotalShoppers.html')
