def apply_twice(func, x):
    return func(func(x))

# Example function
def square(n):
    return n * n

result = apply_twice(square, 2)

print(result)