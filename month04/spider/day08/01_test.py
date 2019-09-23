import execjs

with open('translate.js','r') as f:
    js_data = f.read()

exec_obj = execjs.compile(js_data)
result = exec_obj.eval('e("hell")')
print(result)