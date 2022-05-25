for _ in range(int(input())):
    n=int(input())
    arr=input().split()
    temp=[]
    length=0
    for i in range(n+1):
        for j in range(i):
            temp.append(arr[j:i])
            length+=1
    count=0
    for i in temp:
        for j in i:
            if len(i)==int(j):
                count+=1
                
                break
    print(count)