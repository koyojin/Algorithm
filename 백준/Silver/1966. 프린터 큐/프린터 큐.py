import sys
from collections import deque

T=int(sys.stdin.readline())
for _ in range(T):
    n,m=map(int,sys.stdin.readline().split())
    imp=list(map(int,sys.stdin.readline().split()))
    queue=deque([])
    for idx, val in enumerate(imp):
        queue.append([idx,val])

    cnt=0
    while True:
        curr=queue.popleft()
        if queue and curr[1]<max(v for  i,v in queue):
            queue.append(curr)

        elif curr[0]==m:
            cnt+=1
            break
        else:
            cnt+=1

    print(cnt)