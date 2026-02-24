d = {"a": 1, "b": 2, "c": 1, "d": 3}
target=int(input("Enter the target number: "))
result=[]
for key,values in d.items():
    if(values == target):
        result.append(key)
print(result)
