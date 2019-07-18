import  os
import sys

data = ""
for item in os.listdir("./tcp/dir"):
    data = data + item + "\n"
print(data)