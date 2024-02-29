class FibonacciContainer:
    def __init__(self, n):
        self.fibonacci_numbers = self.generate_fibonacci_sequence(n)

    def generate_fibonacci_sequence(self, n):
        fibonacci_sequence = [0, 1]
        for i in range(2, n):
            next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
            fibonacci_sequence.append(next_number)
        return fibonacci_sequence

    def __len__(self):
        return len(self.fibonacci_numbers)

    def __getitem__(self, index):
        return self.fibonacci_numbers[index]

fib_container = FibonacciContainer(10)

print("Length of the container:", len(fib_container))

print("First 5 Fibonacci numbers:", fib_container[:5])
