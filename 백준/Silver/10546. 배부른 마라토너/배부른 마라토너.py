import sys
n=int(input())
enlisted={}
for i in range(n):
    k=sys.stdin.readline().rstrip()
    if k in enlisted:
        enlisted[k]+=1
    else:
        enlisted[k]=1

for i in range(n-1):
    k=sys.stdin.readline().rstrip()
    if enlisted[k]==1:
        del enlisted[k]
    elif k in enlisted:
        enlisted[k]-=1
print(*enlisted)
    