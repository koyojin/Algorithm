import sys

n,m= map(int,sys.stdin.readline().split())
res=[0]*m
lst= list(range(1, n+1))

def DFS(L):
    if L==m:
        for i in res:
            print(i, end= ' ')
        print()

    else:
        for i in lst:
            res[L]=i
            DFS(L+1)    

DFS(0)

