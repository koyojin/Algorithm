import sys

n,s= map(int,sys.stdin.readline().split())
lst=list(map(int,sys.stdin.readline().split()))
cnt=0

def DFS(v,sum):
    global cnt
    if v==n:
        if sum==s:
            cnt+=1
    else:
        DFS(v+1, sum+lst[v])
        DFS(v+1, sum)

DFS(0,0)
print(cnt if s!=0 else cnt-1)