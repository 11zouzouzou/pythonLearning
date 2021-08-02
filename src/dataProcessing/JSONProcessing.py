import json

import jmespath

# parse
jsonstring = '{"name": "erik", "age": 38, "married": true}'
data = json.loads(jsonstring)
print('dict',data,type(data))
#encoding
encodingData = {'name': 'erik', 'age': 38, 'married': True}
print('string',json.dumps(encodingData,indent=2))# indent 控制缩进

# echo "{ \"name\": \"Monty\", \"age\": 45 }" python3 -m json.tool
# 写入json
writeData = {'name': 'zou', 'age': 18 }
with open('sources/writeData.json','w') as json_file:
  json.dump(writeData,json_file,indent=2)
  print(writeData)
# 读取json
data={}
with open('sources/map.json') as json_file:
  data = json.load(json_file)
  print(data)
# json查询
j = { "people": [{ "name": "erik", "age": 38 },{ "name": "rob", "age": 14 }] }
print( jmespath.search('people[0].age', j))
print(jmespath.search("people[*].age", j))
print(jmespath.search("people[?name=='erik'].age", j))
