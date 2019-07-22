import json

js = json.dumps({"a": 1, "b": 2})  # 将字典转化为json
print(js)

print(json.loads(js))  # 将json转化为字典
