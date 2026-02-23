# from collections import Counter
#
# def fre1(l1):
#     return list(Counter(l1).items())
#
# l1=input().split()
# print(fre1(l1))

def freq(lst):
    fre={}
    for item in lst:
        if item in fre:
            fre[item]+=1
        else:
            fre[item]=1

    return [(key,value) for key,value in fre.items()]

print(freq([1,2,3,4,5,1,2]))