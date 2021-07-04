N = int(input())
A = list(map(int, input().split()))
x = 0
for i in range(N-1):
    for j in range(N-i):
        if A[i] != A[i+j]:
            x += 1
print(x)