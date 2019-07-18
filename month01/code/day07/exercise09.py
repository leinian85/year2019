'''
函数
'''
def print_trigon(count,char):
    '''
    打印直角三角形
    :param count: count: 三角形的直边长
    :param char: 填充的字符
    :return:
    '''
    for r in range(count):
        for c in range(0,r+1):
            print(char,end=" ")
        print("")

print_trigon(5,"#")