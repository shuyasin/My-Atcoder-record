N = int(input())
m = 0
for i in range(N):
    i += 1
    m += i
    if m >= N:
        break
print(i)