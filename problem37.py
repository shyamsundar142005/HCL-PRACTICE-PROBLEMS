def fibonacci(a):
    a, b = 0, 1
    for i in range(a):
        yield a
        a, b = b, a + b
a = int(input("Enter n: "))
for num in fibonacci(a):
    print(num, end=" ")