for _ in range (int(input())):
    N,X=map(int,input().split())
    S=[]
    R=[]
    for i in range(N):
        s,r=map(int,input().split())
        S.append(s)
        R.append(r)
    m=0
    for i in range(N):
        if S[i]<=X:
            m=max(m,R[i])
    print(m)