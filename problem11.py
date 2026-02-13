t=tuple(map(int,input().split()))
list=[]
if(len(t)%2==0):
    for i in range(0,len(t)-1,2):
        list.append((t[i],t[i+1]))
    print(list)
else:
    for i in range(0,len(t)-2,2):
        list.append((t[i],t[i+1]))
    print(list)