import json
import random
# int
print(int('11'))
print(str(200))
print(int(2.3))
print(random.randint(1, 10))  # 1~10随机数
if isinstance(2, int):
    print('2是整数')
# Tuple
mixedTuple = ('Hello', 123, True)
listTuple = tuple([0, 1, 2])
l1 = [1, 2, 3]
l2 = [4, 5, 6]
tutal = (*l1, *l2)  # *解包
persion = ('zou', 12, False)
name, age, re = persion
persionList = list(persion)  # tuple 转list
persionList2 = [*persion]
persionSet = set(persion)  # tuple 转 set
print(mixedTuple, listTuple, tutal, name, age,
      re, persionList, persionList2, persionSet)
# dictionary
phoneNumbers = {'zou': '0571',
                'li': '0572'}  # create
phoneNumbers['wan'] = '0573'  # add
del(phoneNumbers['li'])  # delete
print(phoneNumbers)
phoneNumbers2 = dict([('zou', '0'),
                      ('zou1', '1'),
                      ('zou2', '2')])  # create
comprehension = {x: x**2 for x in (2, 4, 6)}  # {2: 4, 4: 16, 6: 36}
names = ('lei', 'lei2', 'lei3')
namesSet = dict.fromkeys(names, None)
namesKey = dict.keys(namesSet)  # 拿到的是索引zou3 后续创建的zou3 也会存在
namesSet['zou3'] = '3'
print(namesSet)
print(namesKey)

jsonString = '{"name":"zouzouzou","age":38}'
jsonSet = json.loads(jsonString)
print(jsonSet)


config = {'host': 'example.org', 'a': 'z'}
config.get('port', 80)  # default value 80
config.get('schema')  # dafault value None
print(sorted(config), list(config))# list() 按插入顺序sorted() 返回所有键，同时 返回按字母顺序排序的所有键
hasHost = 'host' in config  # True
isEmptyHost = 'host' not in config  # False
print(hasHost, isEmptyHost)
print(config.items())
for key, value in config.items():
    print(key, value)
dict1 = { 'a': 1, 'b': 2 }
dict2 = { 'b': 3, 'c': 4 }
merged = { **dict1, **dict2 }
print (merged)#合并字典
