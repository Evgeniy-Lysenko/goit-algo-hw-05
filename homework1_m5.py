# fibonachi
def caching_fibonacci(): # The function returns a Fibonacci function with caching
    cache = {}

    def fibonacci(n): # The function returns the n-th Fibonacci number
        if n in cache: # Check if the result is already cached
            return cache[n]
        if n <= 1: 
            return n
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2) # Calculate Fibonacci number recursively
        return cache[n]
    
    return fibonacci
fibonacci = caching_fibonacci() # Get the Fibonacci function with caching
fib_input = int(input("Введіть число для обчислення числа Фібоначчі: ")) # Input from user
print(f"Число Фібоначчі для {fib_input} = {fibonacci(fib_input)}") # Print the Fibonacci number for the input
print(fibonacci(fib_input + 2))