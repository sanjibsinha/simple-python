### ### 

def write_Fibonacci_series_up_to_n(n):   
    """Writing Fibonacci series""" 
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()

write_Fibonacci_series_up_to_n(10)

def return_Fibonacci_series(n):   
    """Returning Fibonacci Series"""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

print(return_Fibonacci_series(100))