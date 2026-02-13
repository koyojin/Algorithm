import sys

n,m=map(int,sys.stdin.readline().split())
lst=list(range(1,n+1))
res=[0]*m
ck=[0]*(n+1)

def DFS(L):
    if L==m:
        print(*(res))

    else:
        for i in range(1, n + 1):
                    if ck[i] == 0:  
                        ck[i] = 1  
                        res[L] = i
                        DFS(L + 1)  
                        ck[i] = 0

DFS(0)