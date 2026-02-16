list1=list(map(int,input().split()))
k=int(input())
n=len(list1)
if(n!=0):
    k=k%n

    for i in range(k):
        last=list1.pop()
        list1.insert(0,last)
print(list1)