def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b
n = int(input("Enter n: "))
for num in fibonacci(n):
    print(num, end=" ")