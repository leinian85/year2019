from lxml import etree
html = """
<div class="wrapper">
	<a href="/" id="channel">新浪社会</a>
	<ul id="nav">
		<li><a href="http://domestic.sina.com/" title="国内">国内</a></li>
		<li><a href="http://world.sina.com/" title="国际">国际</a></li>
		<li><a href="http://mil.sina.com/" title="军事">军事</a></li>
		<li><a href="http://photo.sina.com/" title="图片">图片</a></li>
		<li><a href="http://society.sina.com/" title="社会">社会</a></li>
		<li><a href="http://ent.sina.com/" title="娱乐">娱乐</a></li>
		<li><a href="http://tech.sina.com/" title="科技">科技</a></li>
		<li><a href="http://sports.sina.com/" title="体育">体育</a></li>
		<li><a href="http://finance.sina.com/" title="财经">财经</a></li>
		<li><a href="http://auto.sina.com/" title="汽车">汽车</a></li>
	</ul>
</div>
"""

# 1.匹配所有a节点文本内容
parse_html =etree.HTML(html)
e_list = parse_html.xpath('//a/text()')
print(e_list)

# 提取所有的href的属性值
a_list = parse_html.xpath('//a/@href')
print(a_list)

# 提取所有的href的属性值
a_list = parse_html.xpath('//li//a/@href')
print(a_list)

# 提取图片,军事...不包括新浪社会
a_list = parse_html.xpath('//li/a/text()')
print(a_list)