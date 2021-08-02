from os import path
import yaml
with open('sources/config.yaml','r') as yaml_file:
  prime_service = yaml.safe_load(yaml_file)
  print(prime_service)

names_yaml = """
- 'zou1'
- 'zou2'
"""
names = yaml.safe_load(names_yaml)
print(names)

with open('sources/writeYaml.yaml','w') as file:
  yaml.dump(names,file)
print(open('sources/writeYaml.yaml').read())