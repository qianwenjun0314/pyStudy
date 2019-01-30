import os

from click._compat import raw_input

# str2 = raw_input('请输入：')
# print('你输入的内容是：' + str2)
#
#
# str1 = input("请输入：")
# print("你输入的内容是: " + str1)

f1 = open('../../resource/text.txt')

print("文件名: ", f1.name)
print("是否已关闭 : ", f1.closed)
print("访问模式 : ", f1.mode)

f2 = open('../../resource/text.txt', 'r+')

print("文件名: ", f2.name)
print("是否已关闭 : ", f2.closed)
print("访问模式 : ", f2.mode)

f2.write('test write2\n')
f1str = f2.read(10000)
print('读取的内容为：\n',f1str)


# f3 = open('../../resource/text.txt', 'r+')
# os.rename('../../resource/qwj1.txt','../../resource/qwjChange1.txt')
os.mkdir('../../resource/','testdir1')
