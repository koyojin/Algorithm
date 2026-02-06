import sys

n=int(sys.stdin.readline())
stack=[]
def bi(x):
    if x>0:
        bi(x//2)
        stack.append(x%2)

bi(n)
for i in stack:
    print(i, end='')