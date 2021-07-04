A,B = (int(x) for x in input().split())
if A > B:
    print('No')
elif A*6 >= B:
    print('Yes')
elif A*6 < B:
    print('No')