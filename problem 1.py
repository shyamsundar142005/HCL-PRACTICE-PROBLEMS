s="ababa"
sub="aba"
count=0
for i in range(0,len(s)):
    if(s[i:len(sub)+i]==sub):
        count+=1
print(count)
