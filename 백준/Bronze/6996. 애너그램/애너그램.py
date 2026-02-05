import sys
from collections import Counter
n=int(sys.stdin.readline())
for _ in range(n):
    a,b = map(str, sys.stdin.readline().split())
    if Counter(list(a))==Counter(list(b)):
        print("{} & {} are anagrams.".format(a,b))
    else:
        print("{} & {} are NOT anagrams.".format(a,b))