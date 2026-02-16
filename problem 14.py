list1=list(map(int,input().split()))
list2=list(map(int,input().split()))
list3=[]
if(len(list1)==None or len(list2)==None):
    print("[]")
if(len(list1)<=len(list2)):
    for i in range(len(list1)):
        list3.append(list1[i])
        list3.append(list2[i])
    print(list3)
else:
    for i in range(len(list2)):
        list3.append(list1[i])
        list3.append(list2[i])
    print(list3)