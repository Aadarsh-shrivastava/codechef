for _ in range (int(input())):
    a,b,a1,b1,a2,b2=map(int,input().split())
    print('1' if (a1==a or a1==b) and (b1==a or b1==b) else  '2' if (a2==a or a2==b) and (b2==a or b2==b) else '0')
    