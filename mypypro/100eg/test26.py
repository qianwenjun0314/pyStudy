def test25():
    n = int(input('请出入n值：'))

    sun = 0

    for i in range(1,n+1):
        if i == 1:
            sun = 1
        else:
            sun = sun * i
            print('第%s个数的累积为%s'%(i,sun))

test25()