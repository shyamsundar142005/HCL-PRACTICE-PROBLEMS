def aggregate(*nums,op="sum"):
    if not nums:
        return None
    if op=="sum":
        return sum(nums)
    elif op=="avg":
        return sum(nums)/len(nums)
    elif op =="max":
        return max(nums)
    else:
        return "Invalid Operation"
print(aggregate(1,2,3,4,5))
print(aggregate(1,2,3,4,5,6,op="max"))
print(aggregate(1,2,3,4,5,6,op="avg"))