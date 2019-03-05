data = input('请输入一个五位数：')
s = str(data)
l = len(s)
print(l)


def test30():
    if l%2 == 0:
        for i in range(0,int(l/2)):
            if s[i] != s[-1-i]:
                print(False)
                break
        print(True)

    else:
        for i in range(0, int((l-1)/ 2)):
            if s[i] != s[-1 - i]:
                print(False)
                break
        print(True)


def zhi():
    for i in range(0,int(l/2)):
        if s[i] != s[-1-i]:
             print(False)
             break
    print(True)


test30()
zhi()