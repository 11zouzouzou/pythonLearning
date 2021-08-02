# Function
# #Forced keyword arguments
def forcedKeyWordArg(*, a, b):
    print(a, b)


forcedKeyWordArg(a=1, b=2)
# #Using * and ** for function arguments


def using(a, b):
    print('using**and*', a, b)


args = {'a': 'zou', 'b': 'lei'}
using(**args)
l = [1, 2]
using(*l)

# #decorating(装饰) your functions


def printArg(func):
    def wrapper(num):
        print('arg for', func.__name__, 'is', num)
        return func(num)
    return wrapper


@printArg
def addOne(x):
    print('add', x)
    return x+1


print(addOne(1))

# #anonymous(匿名) functions

addNumbers = [1, 2, 3]
anonymous = map(lambda x: x+1, addNumbers)

print('匿名函数', anonymous, list(anonymous))

# #list comprehensions <expression> for item in list if <conditional> }
print([x for x in range(1, 5)])
print(list(range(1,5)))
print([x for x in range(1,10) if x % 2 == 0])
print([x + 4 for x in [10, 20]])
def some_function(a):
    return (a + 5) / 2

sFunc = [some_function(i) for i in range(8)]
print(sFunc)
m = [[j for j in range(3)] for i in range(4)]
print(m)
print([value for sublist in m for value in sublist])

# #Python iterator
my_iterable = range(1, 3)#可迭代对象
my_iterator = my_iterable.__iter__()
my_iterator.__next__()
my_iterator.__next__()
# my_iterator.__next__()#无下一个迭代对象了
class EvenNumbers:
    last = 0
    def __iter__(self):
        return self
    def __next__(self):
        self.last += 2
        if self.last > 8:
            raise StopIteration
        return self.last
en = EvenNumbers()#迭代器
for num in en:
    print(num)  