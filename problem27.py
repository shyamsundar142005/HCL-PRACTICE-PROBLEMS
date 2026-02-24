n=int(input("Enter the size of an tuple: "))
data=[]
for i in range(n):
    item=input("Enter the item name: ")
    category=input("Enter the category name: ")
    data.append((item,category))
grouped={}
for item,category in data:
    if category in grouped:
        grouped[category].append(item)
    else:
        grouped[category]=[item]
print(grouped)