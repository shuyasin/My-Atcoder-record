N,Q = (int(x) for x in input().split())
A = list(map(int, input().split()))
K = [int(input()) for i in range(Q)]
x = []
for i in range(100):
    if A == i:
        pass
    else:
        x.append(i)
print(x)
