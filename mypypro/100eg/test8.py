#9*9乘法口诀表

def test8():
    for i in range(1,10):
        for j in range(1,i+1):
            if i==j:
                print('%d*%d=%d' % (i, j, i * j), end='\n')
            else:
                print('%d*%d=%d'%(i,j,i*j), end=' ')


test8()