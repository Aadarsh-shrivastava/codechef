# cook your dish here
import math
for _ in range (int(input())):
    # A,B,m=map(int,input().split())
    N=int(input())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    count=0
    
    
    for i in range (N-1):
        # for j in range(i+1,N):
            #print(A[i],B[i])
        if(A[i]==B[N-i-1] and A[N-i-1]==B[i] ):
            count+=1
               
    print(count)