import time
#  每个 Python 程序至少有一个线程：主线程。您将在下面找到单线程版本，它是我们速度方面的基准。它按顺序运行我们的重函数 80 次
# A CPU heavy calculation, just
# as an example. This can be
# anything you like
def heavy(n, myid):
    for x in range(1, n):
        for y in range(1, n):
            x**y
    print(myid, "is done")
 
def sequential(n):
    for i in range(n):    
        heavy(500, i)
 
if __name__ == "__main__":
    start = time.time()
    sequential(30)
    end = time.time()
    print("Took: ", end - start)#my mac 21s