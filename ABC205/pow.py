A,B,C = (int(x) for x in input().split())
if C % 2 != 0:
    if A > B:
        print('>')
    elif A < B:
        print('<')
    elif A == B:
        print('=')
else:
    if abs(A) > abs(B):
        print('>')
    elif abs(A) < abs(B):
        print('<')
    elif abs(A) == abs(B):
        print('=')