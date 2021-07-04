N,K = (int(x) for x in input().split())
a = list(map(int, input().split()))
b = []
for i in range(N):
    for j in range(K):
        if K != 0:
            b[j] += 1
            K = K-1
print(b)     