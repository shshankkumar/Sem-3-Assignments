def fibonacci(n, memo={}):
    if n <= 1:
        return n

    if n in memo:
        return memo[n]

    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]


# Accept N from user
N = int(input("Enter the value of N: "))

# Generate first N Fibonacci numbers
sequence = []

for i in range(N):
    sequence.append(fibonacci(i))

# Display the sequence
print("Fibonacci Sequence:", sequence)


'''output:
Enter the value of N: 12
Fibonacci Sequence: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]  '''