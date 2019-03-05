#题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
#程序分析：利用 while 或 for 语句,条件为输入的字符不为 '\n'。
import string


def test17():
    s = input('请输入一串字符串：\n')

    data1 = 0
    data2 = 0
    data3 = 0
    data4 = 0
    i = 0

    for i in s:
        if i.isdigit():
            data1+=1
        elif i.isalpha():
            data2+=1
        elif i.isspace():
            data3+=1
        else:
            data4+=1
    print('数字的个数为：%s,字母的个数为：%s,空格的个数为：%s,其他字符的个数为：%s'%(data1,data2,data3,data4))

test17()