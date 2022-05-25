for _ in range (int(input())):
    n,f,v,m=map(int,input().split())
    print('YES' if v>=n and f+m>=n else 'NO')
    