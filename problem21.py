s=input("Enter the string: ")
freq={}
for item in s:
    if item in freq:
        freq[item]+=1
    else:
        freq[item]=1
print(freq)