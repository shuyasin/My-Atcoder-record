import math
N = int(input())
x = math.floor(1.08 * N)
if x < 206:
    print('Yay!')
elif x == 206:
    print('so-so')
elif x > 206:
    print(':(')
