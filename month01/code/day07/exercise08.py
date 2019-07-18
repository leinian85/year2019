list01 = ["香蕉","苹果","水蜜桃"]
list02 = ["牛奶","可乐"]
list03 = [list01[i]+list02[j] for i in range(len(list01)) for j in range(len(list02))]
print(list03)