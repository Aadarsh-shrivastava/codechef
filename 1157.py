# # cook your dish here
# for _ in range(int(input())):
#     n=int(input())
#     #a,b,c,d=map(int,input().split())
#     arr=input().split()
#     for i in range(n-1,-1,-1):
#         if(arr[i]=='0'):
#             pass
#         else:
#             print(i)
#             break


# import math
# for _ in range(int(input())):
#     n=int(input())
#     arr=input()
#     n=n-1
#     count=0
#     mid=math.floor(n/2)
#     print(mid)
#     for i in range(mid+1):
#         print(arr[i],'---',arr[n-i])
#         if(arr[i]!=arr[n-i]):
#             count+=1
    
#     print(int(count/2) if count%2==0 else int((count+1)/2))   

from pickle import TRUE


def binary_val(x):
    val=[]
    if(x%2!=0):
        val=[1]
    else:
        val=[0]
    while x>1:
        x=x//2
        print(x%2)
        val.append(x%2)
    return val


for _ in range(int(input())):
    n=int(input())
    arr2=input().split()
    arr = [int(item) for item in arr2]
    # print(binary_val(n))
    count=0
    while sum(arr)>0:
        if 0 in arr:
            arr.remove(0)
        mn=min(arr)
        print('min is',mn)
        for i in arr:
            if i%2!=0:
                i-1
        bv=binary_val(mn)
        bv2=[]
        print('binary of minimu',bv)
        count+=sum(bv)
        print('count',count)
        pw=0
        
        for i in bv:
            bv2.append(i*pow(2,pw))
            pw+=1
        print(bv2)    
        N=0
        for i in arr:
            arr[N]-=sum(bv2)
            if(arr[N]<0):
                arr[N]=0
            N+=1    
        print(arr)
        
            



        
