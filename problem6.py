sentence=input("Enter the sentence: ")
result=" "
for ch in sentence:
    if(ch.isdigit()):
        result+="#"
    else:
        result+=ch
print(result)