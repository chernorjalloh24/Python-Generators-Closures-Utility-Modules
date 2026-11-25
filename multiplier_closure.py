# Function that creates a multiplier
def make_multiplier(factor):

    # Inner function that remembers the factor
    def multiply(x):
        return x * factor

    return multiply


# Create two multiplier functions
times3 = make_multiplier(3)
times10 = make_multiplier(10)

# Test the multiplier functions
print("===== MULTIPLIER CLOSURE =====")

print("3 multiplied by 7 =", times3(7))
print("10 multiplied by 7 =", times10(7))
