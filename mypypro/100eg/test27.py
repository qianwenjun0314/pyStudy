s = str(input('输入字符串：'))


def test27(s):
    print(s)
    l = list(s)
    print(l.reverse())
    print(l)





def digui(s):

    if len(s)<1:
        print(s)
        return s
    else:
        s3 = digui(s[1:])+s[0]
        print(s3)
        return s3



test27(s)
digui(s)