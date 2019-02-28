class People(object):
    #类变量可以由所有的对象访问，但是对象只能访问，不能修改
    #可以用来做资源共享
    total=6
    name = 'python 8期'
    #初始化函数，添加对象属性
    def __init__(self,name,age,school):
        #给对象属性赋值
        self.name=name
        self.age=age
        self.school=school
        #只能使用类去修改
        People.total+=1


# p1和p2是两个不同的对象，这两个对象各自的信息时不可以共享的
p1 = People('张三', 21, '**大学')
print(p1.total)
p2 = People('钊冉', 22, '***大学')
print(p2.total)
# 类无法访问对象实例的属性
# print(People.name)
# 对象可以访问类属性/类变量
# print(p1.total)
# 对象没有办法修改类的属性值
# 给p1添加了一个total属性
# p1.total=100
print(People.total)

#类对象和实例对象，都可以动态的增加属性和删除属性
p2.family = 'xihu'
People.work = 'china'
print(p2.family)
print(People.work)


print(p1.name, p1.age, p1.school)
print(p1.__dict__)

#此时是给实例对象，新增了total属性，但是并不改变类属性total的值
p1.total = 100
print(p1.name, p1.age, p1.school, p1.total)
print(p1.__dict__)
print(People.total)



