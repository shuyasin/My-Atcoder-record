import math
P = int(input())
cnt = 0
for i in range(10,0,-1):
    a = math.factorial(i)
    if P >= a:
        while P >= a:
            P = P - a
            cnt += 1
print(cnt)