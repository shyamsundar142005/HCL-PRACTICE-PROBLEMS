n=int(input("Enter the size of an list: "))
arr=[]

for i in range(n):
    arr.append(int(input("Enter the element of an array: ")))
seen=set()
result=[]
for i in range(n-1,-1,-1):
    if( arr[i] not in seen):
        seen.add(arr[i])
        result.append(arr[i])
result.reverse()
print(result)