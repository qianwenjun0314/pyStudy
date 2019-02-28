class Dog:

    def __init__(self, age = 0):
        self.age = age
    # 类实例方法
    # 最常见的实例方法
    def bark(self, y):
        print (self.age, y)

    # 类方法
    #cls即为类自身
    @classmethod
    def eat(cls, food):
        print(cls, food)


    #静态方法
    #不能传递和类或实例相关的参数，如cls或self，但可以传递其他参数
    @staticmethod
    def sleep(age):
        print(Dog(age).age)


dog = Dog(5)

#Dog.bark(3)
Dog.eat('tomato')
Dog.sleep(99)

dog.bark(10)
dog.eat('meet')
dog.sleep(100)



