def counter():
    count = 0

    def next():
        nonlocal count
        count += 1
        return count

    return next


c = counter()

print(c())
print(c())
print(c())
print(c())