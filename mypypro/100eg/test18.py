import math
def test18():
    a = int(input('请输入第一个字符：'))
    n = int(input('请输入次数：'))

    add = a
    data = a

    for i in range(2,n):
        data += a * math.pow(10, i-1)
        add += data
        print('a的值为：%s'%data)
    print(add)


test18()