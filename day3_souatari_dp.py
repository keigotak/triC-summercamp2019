'''
5
1 5 7 10 21
4
2 4 17 8
'''

n = int(input())
a = [int(x) for x in input().split()]
q = int(input())
m = [int(x) for x in input().split()]

memo = set()

for mi in m:
    for i in range(len(a)):


