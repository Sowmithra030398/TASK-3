# Define the Fibonacci function with a base case handling
fibnocci_sequence = lambda x: x if x <= 1 else fibnocci_sequence(x-1) + fibnocci_sequence(x-2)

# Print the first 10 Fibonacci numbers
for i in range(50):
    print(fibnocci_sequence(i))