list=list(map(int,input().split()))
total=0
for i in range(len(list)):
    if(list[i]<=0):
        list[i]=0
    else:
        total=total+list[i]
        list[i]=total
print(list)
