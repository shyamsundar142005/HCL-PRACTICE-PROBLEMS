def count_up_to(n):
    for i in range(1,n+1):
        yield i*i
g=count_up_to(5)
print(next(g))
print(next(g))
