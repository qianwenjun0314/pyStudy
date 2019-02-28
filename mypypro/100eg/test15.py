def test5():
    score = int(input('请输入：'))
    if score >= 90:
        grade = 'A'
    elif score >=80:
        grade = 'B'
    else:
        grade = 'C'
    print('%d分数的等级为:%s'%(score,grade))

test5()