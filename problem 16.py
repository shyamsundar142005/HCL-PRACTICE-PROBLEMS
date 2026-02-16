list1=list(input().split())
for i in range(len(list1)):
    list1[i]=list1[i].lower()
list1=sorted(set(list1))
print(list1)