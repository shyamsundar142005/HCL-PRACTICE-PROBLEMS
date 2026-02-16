list1=list(map(int,input().split()))
list2=[]
for i in range(len(list1)):
    if(list1[i]%2==0):
        list2.append(list1[i]**2)
print(list2)