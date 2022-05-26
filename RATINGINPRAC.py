for _ in int(input()):
    n=int(input())
    a=list(map(int,input().split()))
    print("Yes" if a==sorted(a) else "No")