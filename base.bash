echo "You can list numbers and text like this:"
 
for n in 1 2 3 four
do
  echo "Number $n"
done
 
echo "Or specify a range of numbers:"
 
for n in {1..5}
do
  echo "Number $n"
done
 
echo "Or use the output of another command:"
for f in $(ls)
do
  echo $f
done

if test -z "$1"#如果一个变量的长度为零
then
  echo "Usage: $0 <Your name>"
else
  echo "Hello $1, from $0"
fi

for i in {1..10}
do
  if test $i -eq 3 #比较两个值以查看它们是否相同
  then
    echo "I found the 3!"
  fi
done