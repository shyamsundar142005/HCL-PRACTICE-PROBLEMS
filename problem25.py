s=input("Enter the sentence: ")
words=s.split()
freq={}
for word in words:
    if word in freq:
        freq[word]+=1
    else:
        freq[word]=1
sorted_freq=sorted(freq.items(),key=lambda x:x[1],reverse=True)
print(sorted_freq)