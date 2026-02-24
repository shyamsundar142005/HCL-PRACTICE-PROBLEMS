s=input("Enter the string: ")
words=s.split()
result=[]
freq={}
for word in words:
    if (word in freq):
        freq[word]+=1
    else:
        freq[word]=1
print(freq)