#數字倒金字塔
n = eval(input())
for i in range(n+1,0,-1):
    for j in range(n-i+1, 0,-1):
        print('    ', end = ' ')
    for a in range (i-1,0,-1):
        print(a, end='    ')
    for k in range(0, i-2,1):
        print(k+2, end='    ')

    print()
