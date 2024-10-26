def fibonacci(n):
    sequence = []
    a, b = 1, 2
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Example: Generate the first 10 terms of the Fibonacci sequence
n_terms = 10
print(f"First {n_terms} terms of the Fibonacci sequence:", fibonacci(n_terms))
