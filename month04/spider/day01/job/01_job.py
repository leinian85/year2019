import re
import hashlib

html = '''
<div class="animal">
    <p class="name">
		<a title="Tiger"></a>
    </p>
    <p class="content">
		Two tigers two tigers run fast
    </p>
</div>

<div class="animal">
    <p class="name">
		<a title="Rabbit"></a>
    </p>

    <p class="content">
		Small white rabbit white and white
    </p>
</div>
'''
a = '123'
a.rstrip()
pattern = re.compile('<div class="animal">.*?title="(.*?)".*?<p class="content">(.*?)</p>',re.S)
r_list = pattern.findall(html)
r_list_new = [(name,content.strip()) for name,content in r_list]
print(r_list_new)

for name,content in r_list_new:
    print("动物名称 ：",name)
    print("动物名称 ：",content)
    print("*"*40)

