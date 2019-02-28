def fib(n):

    if n==1:
        return [1]
    if n==2:
        return [1,1]
    fibs = [1,1]
    for i in range(2,n):
        #尾部两位数相加
        fibs.append(fibs[-1] + fibs[-2])
    print(fibs)


fib(10)
