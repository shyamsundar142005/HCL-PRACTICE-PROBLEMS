s=input("Enter the string: ")
freq={}
result=[]
for char in s:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1
for key,value in freq.items():
    if(value==1):
        result.append(key)
print(result)