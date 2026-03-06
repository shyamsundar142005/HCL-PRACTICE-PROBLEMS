def gen_numbers():
    for i in range(1, 11):
        yield i
def gen_squares(numbers):
    for num in numbers:
        yield num * num
for square in gen_squares(gen_numbers()):
    print(square, end=" ")