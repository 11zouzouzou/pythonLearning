import subprocess
subprocess.run(['ls', '-al'])
result = subprocess.run(['python3', '--version'], capture_output=True,
                        encoding='UTF-8')  # capture_output捕获输出，终端不将输出
print(result)
# #Feeding data from standard input
code = """
for i in range(1, 3):
  print(f"Hello world {i}")
"""
result2 = subprocess.run(['python3'], input=code,
                         capture_output=True, encoding='UTF-8')
print(result2.stdout)
# #Running shell commands #不建议
result3 = subprocess.run(['ls -al | head -n 1'], shell=True)# 有命令注入风险

# #command injection#不建议
thedir = input()
result4 = subprocess.run([f'ls -al {thedir}'],shell=True)#允许任何命令