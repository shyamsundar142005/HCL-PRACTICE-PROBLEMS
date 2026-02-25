from functools import reduce

l1=list(map(int,input().split()))

discounted= list(map(lambda x: x*0.9,l1))
filtered = list(filter(lambda x: x>=200,discounted))
reduced =reduce(lambda x,y:x+y,filtered,0)
print(filtered)
print("Final Bill Amount: ",reduced)