def factorial(n):
	if (n==0 or n==1):
		return 1
	else:
		return n * factorial(n-1)
		
print(factorial(4)) 

def fibo(n):
    if n <= 0:
        return "Invalid input"
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
    
print(fibo(4))


def fibonacci_iterative(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    a, b = 0, 1  # Fibonacci(1) = 0, Fibonacci(2) = 1
    for _ in range(3, n + 1):
        a, b = b, a + b  # Update values

    return b

# Example usage
n = 1000
print(f"Fibonacci number at position {n}: {fibonacci_iterative(n)}")
