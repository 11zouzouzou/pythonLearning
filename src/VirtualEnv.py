import subprocess
# subprocess.run(['python3', '-m','venv','./venv'])# 创建虚拟环境
# #cannot run
# result = subprocess.run(['ls','source ./venv/bin/activate'],shell=True)# 激活
# print(result)
# deactivate 停用
# rm -r venv 删除

#Pip
#pip install --upgrade pip #此命令要求pip安装pip，如果已经安装，则更新它。
#pip freeze > requirements.txt #生成当前环境的依赖项
#pip install -r requirements.txt #安装依赖项
#pip install -i https ://your-custom-repo/simple <包名> #使用 pip install -i 自定义存储库
#pip uninstall -r <requirements file name>
#pip list # 显示包名称和版本。
#pip show <package name> #Show package details

#Pipenv
#pip install --user pipenv or brew install pipenv
#pipenv shell #进入虚拟环境
#pipenv check #检查