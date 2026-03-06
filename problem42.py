def make_multiplier(k):
    def multiply(x):
        return x * k
    return multiply

# Create a multiplier
double = make_multiplier(2)

result = double(5)
print(result)