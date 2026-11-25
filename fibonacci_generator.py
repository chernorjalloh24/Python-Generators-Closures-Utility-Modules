# Generator function to produce Fibonacci numbers
def gen_fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        yield a
        a, b = b, a + b


# Ask the user how many numbers to generate
try:
    n = int(input("How many Fibonacci numbers do you want? "))

    if n <= 0:
        print("Please enter a positive number.")
    else:
        print("\n===== FIBONACCI SEQUENCE =====")

        for number in gen_fibonacci(n):
            print("Fibonacci number:", number)

except ValueError:
    print("Error: Please enter a valid integer.")
