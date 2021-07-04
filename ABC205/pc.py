N = int(input())
A = list(map(int, input().split()))
a = sorted(A)
b = list(range(1,N+1))
if a == b:
    print('Yes')
else:
    print('No')