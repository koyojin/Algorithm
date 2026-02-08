import sys
# print(ord('A'))
n=int(sys.stdin.readline())
tree=[0]*26
for _ in range(n):
    x, l, r = sys.stdin.readline().split() 
    
    left = ord(l) - ord('A') if l != '.' else -1
    right = ord(r) - ord('A') if r != '.' else -1
    
    tree[ord(x) - ord('A')] = [left, right]


def DFS(v):
    if v==-1:
        return
    print(chr(v + ord('A')), end='')    

    DFS(tree_i[v][0])
    DFS(tree_i[v][1])

def mDFS(v):
    if v==-1:
        return

    mDFS(tree_i[v][0])
    print(chr(v + ord('A')), end='')    
    mDFS(tree_i[v][1])


def rDFS(v):
    if v==-1:
        return

    rDFS(tree_i[v][0])
    rDFS(tree_i[v][1])
    print(chr(v + ord('A')), end='')    

cnt=0

for _ in range(3):
    tree_i=tree.copy()
    if cnt==0:
        DFS(0)
    elif cnt==1:
        mDFS(0)
    else:
        rDFS(0)
    cnt+=1
    print()