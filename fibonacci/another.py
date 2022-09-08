import fib

fib.return_Fibonacci_series(10)
print(fib.return_Fibonacci_series(10).__doc__)

fib.return_Fibonacci_series(100)
print(fib.return_Fibonacci_series(100).__doc__)

print(fib.__name__)

'''
0 1 1 2 3 5 8 
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.
Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.

fib
'''