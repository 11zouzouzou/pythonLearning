import subprocess
result1 = subprocess.run(['pwd'])#返回工作目录
result2 = subprocess.run(['ls','-lha'])#目录内容 -l:以长格式列出 -h:将文件大小更改为更具可读性的内容,-a:名称以点 (.) 开头的“隐藏”目录条目显示
#  cp file1.txt file1.txt.bak #复制
#mv file1.txt file1.txt.bak #重命名/移动
#mkdir 制作目录 -p：使用它时，任何尚不存在的中间目录也将被创建
#rm # -rf删除整个
#control+r #查找上一个命令
#cat、less、tail、head:查看内容
#set -u #防止使用未设置的变量
#find . -type f #列文件
#find . -type d #列目录
#find . -type f -mtime +5m #返回 5 分钟前（-:5分钟内）修改过的所有文件 s(second)m(minute)h(hour)d(day)w(week)
#find /path/to/files* -mtime +5m -exec rm {} +  # -exec 标志。它允许我们执行任何命令
#cat <filename> | wc #cat 打印文件的内容。wc 计算它输入的所有行、字和字节。 wc -l，它只计算文件中的行数。sort：排序


# history n	查看n 历史记录中的最多 行
# !!	重复最后一条命令
# !n	重复历史记录中的命令编号 n
# !cd	重新运行您输入的最后一个命令，在本例中为“cd”
# !*	替换上一个命令中的参数