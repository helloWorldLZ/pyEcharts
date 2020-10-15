"""笔记本电脑参数权重雷达图"""

import json
from pyecharts import options as opts
from pyecharts.charts import Radar

featureDescriptionsExtract = []
fileName = 'json/featureDescriptionsExtract.json'
with open(fileName, encoding='utf-8') as f_obj:
    featureDescriptionsExtract = json.load(f_obj)

parameters = ['内存', '处理器', '键盘', '指纹识别', '硬盘', '显卡', '运行']
topK, data, schema = 0, [], []
for item in featureDescriptionsExtract:
    if item[0] in parameters and topK < 7:
        topK += 1
        schema.insert(0, opts.RadarIndicatorItem(name=item[0], color='black', max_=1))
        data.insert(0, item[1])

c = (
    Radar()
    .add_schema(schema)
    .add("实际开销", [data], label_opts=opts.LabelOpts(formatter='123', is_show=True))
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
).render('renderHtml/radar.html')
