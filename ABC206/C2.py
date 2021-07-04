N = int(input())
A = list(map(int, input().split()))
x = 0
for i in range(1,N):
    j = N - (i-2)
    if A[i] != A[i+1] or A[i] != A[j]:
        x += 1
print(x)