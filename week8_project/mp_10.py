# 第10周 现代程序设计

# 作业  类的继承  方法覆盖 重新对方法进行实现
# 体现多态性


# 观察者模式(实现订阅)   观察者和被观察者的抽象耦合
# 被观察者要有一个数据结构的数据结构。 为观察者提供观察功能
# 有一个添加方法和删除方法
# 状态该改变时通知观察者
# 观察者应该有更新行为 
# 将对象分为两类 观察者和被观察者 并分别建立两个类，
# 在这两个类中锋别涉及一些通用方法，让自类进行继承


# 迭代 对数据结构进行遍历（Iterable）
from typing import Iterable


print(isinstance([1,2,3],Iterable))
print('--------------------------------------------')


# 生成器 直接生成列表可能占用大量的内存
# 生成器可以一边循环一遍计算元素

L = [x*x for x in range(10)]
G = (x*x for x in range(10))

print(L)
print(G)
print('--------------------------------------------')

def fib(max):
    n,a,b = 0,0,1
    while(n<max):
        yield b
        a,b = b,a+b
        n+=1
    return 'done'

print(fib(6))
print('--------------------------------------------')

for f in fib(6):
    print(f)
print('--------------------------------------------')

# 生成器使用
f = fib(6)
while 1:
    try:
        print(next(f))
    except StopIteration as si:
        print(si.value)
        break
print('--------------------------------------------')


# 迭代器 生成器一定是迭代器
# 可迭代的不一定是迭代器 可表示无限大的数据流

# 如何创建（在类中加入__iter__,__next__,__reversed__等专有方法)
