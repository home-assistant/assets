def fibonacci(n):
    """Calculate the fibonacci number for a given integer."""
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a+b
    return a

def main():
    x = int(input('Please enter an integer: '))
    print(fibonacci(x))

if __name__ == "__main__":
    main()

