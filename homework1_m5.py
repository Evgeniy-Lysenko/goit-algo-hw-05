# fibonachi 
def caching_fibonacci(): # The function returns a Fibonacci function with caching
    cache = {}

    def fibonacci(n): # The function returns the n-th Fibonacci number
        if n in cache: # Check if the result is already cached
            return cache[n]
        if n <= 0: 
            return 0
        if n == 1:
            return 1
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2) # Calculate Fibonacci number recursively
        return cache[n]
    
    return fibonacci

def main():
    fibonacci = caching_fibonacci() # Get the Fibonacci function with caching

    while True:
        fib_input = input("Введіть число для обчислення числа Фібоначчі або Exit для виходу: ") # Input from user
        try:
           if fib_input.lower() == 'exit': # Exit condition
               break
           fib_input = int(fib_input) # Convert input to integer
           print(f"Число Фібоначчі для {fib_input} = {fibonacci(fib_input)}") # Print the Fibonacci number for the input
        except ValueError:
            print("Будь ласка, введіть коректне число або 'Exit' для виходу.") # Error message for invalid input
            continue

if __name__ == "__main__":
    main()