#将一个字符转换为它的整数值
print(ord('a'))

#将序列 s 转换为一个元组
list1 = [123, 'xyz', 'zara', 'abc']
list2 = {1:2,3:4}
list3 = (1,2,3,4)
print(tuple(list1))
print(tuple(list2))
print(tuple(list3))

Money = 2000

def AddMoney():
    # 想改正代码就取消以下注释:
    # global Money
    Money1 = 1000
    # Money = Money + 1


print(Money)
AddMoney()
print(Money)
