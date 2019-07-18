def transform_weight(weight):
    '''
    将两转换成几斤几两   16进制
    :param weight: 两
    :return:元组(斤,两)
    '''
    num1 = weight // 16
    num2 = weight % 16
    return (num1,num2)
num1,num2 = transform_weight(20)
print('%d斤%d两'%(num1,num2))