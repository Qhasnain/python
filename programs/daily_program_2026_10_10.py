# Automatically generated daily program
# Date: 2026-10-10 19:22:26

def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

if __name__ == "__main__":
    print("Fibonacci Sequence (first 10 numbers):")
    print(fibonacci(10))
