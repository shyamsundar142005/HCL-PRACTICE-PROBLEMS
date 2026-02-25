score=list(map(int,input().split()))
weight=list(map(int,input().split()))
multiplied=list(map(lambda x,y: x*y,score,weight))
sumed=sum(multiplied)
weight_sum=sum(weight)
result=sumed/weight_sum
print(result)