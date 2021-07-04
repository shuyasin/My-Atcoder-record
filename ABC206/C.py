N = int(input())
A = list(map(int, input().split()))
x = 0
for i in range(N):
    for j in range(N-1):
        if A[i] != A[j+1]:
            if i < j+1:
                x += 1 
            else:
                break  
print(x)