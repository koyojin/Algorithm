import sys

n=int(sys.stdin.readline())
cal=list[str](map(str,sys.stdin.readline().rstrip()))

val=[]
for i in range(n):
    val.append(sys.stdin.readline().rstrip())

stack=[]
for e in cal:
    if e.isalpha():
        stack.append(val[ord(e)-ord("A")])
    else:
        b=stack.pop()
        a=stack.pop()
        res=eval(a+e+b)
        stack.append(str(res))

print(f"{res:.2f}")