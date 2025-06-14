def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def main():
    try:
        num_terms = int(input("Enter the number of Fibonacci terms to generate: "))
        if num_terms <= 0:
            print("Please enter a positive integer.")
        else:
            gen = fibonacci_generator()
            print("Fibonacci Sequence:")
            for _ in range(num_terms):
                print(next(gen), end=" ")
            print()
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
