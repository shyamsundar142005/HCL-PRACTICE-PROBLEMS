abbrevations={"AI","ML","NLP","API"}
sentence=input("Enter a Sentence: ")
words=sentence.split()
result=[]
for i in words:
    if(i.upper() in abbrevations):
        result.append(i.upper())
    else:
        result.append(i.capitalize())
final_sentence=" ".join(result)
print(final_sentence)
