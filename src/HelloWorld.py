print('HelloWolrd --zou')
# object
# print(dir(5))  # 查看5对象的预制方法
print(len('test'))
print('test'.islower())
print('abcd'.replace('a', 'b'))

# 变量
# number
result = 20+20
print('定义变量', type(result), result)
# string
str = 'hello\'WorldString\"dd\"'
print(str.lower())
# function


def sayHi(name, defaultName='Lei'):
    print('Hi:', name, defaultName)


sayHi('Zou')

# Boolean and Conditional Programming
doorIsLocked = True
if doorIsLocked:
    print('doorOpen')
else:
    print('doorClose')
# For loop
for letter in 'zoulei':
    print(letter)
# while loop
mylist = [1, 'z', 'Hello']
i = 0
while i < len(mylist):
    print(mylist[i])
    i = i + 1
