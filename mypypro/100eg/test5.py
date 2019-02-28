def test5():
    l = []
    for i in range(0,3):
        x = int(input('integer:'))
        l.append(x)
    l.sort()
    l.reverse()
    print(l)
    #list.reverse() 的返回值是 None ，它逆序的结果直接体现在原来的列表里面。
    print(l.reverse())
    print(l)

test5()