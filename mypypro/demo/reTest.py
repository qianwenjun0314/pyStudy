import re

class reTest:


    body = 'orderId=906671818793340412&asoind='


    def test1(self):
        pattern = r'\d+'
        # body = 'orderId=906671818793340412&asoind='
        if re.match(pattern, self.body):
            print(self.body)
        else:
            print("false")

    def test2(self):
        pattern = r'\d+'
        # body = 'orderId=906671818793340412&asoind='
        if re.search(pattern, self.body):
            print(self.body)
        else:
            print("false")


    def test3(self):
        pattern = r'[Id=...]'
        if re.search(pattern, self.body):
            print(self.body)
        else:
            print("false")

    def test4(self):
        # pattern = r'orderId=(.*?)&'
        # pattern = r'orderId=(.*)&'
        pattern = r'orderId=(\d{,18})&'

        if re.match(pattern, self.body):
            print('true')
            print(re.match(pattern, self.body).group(0))
            print(re.match(pattern, self.body).group(1))

        else:
            print('false')



# *匹配：表示0次或者很多次
# +匹配：表示1次或者很多次

reTest = reTest()
#类的实例方法，需要类的实例去调用
reTest.test1()
reTest.test2()
reTest.test3()
reTest.test4()