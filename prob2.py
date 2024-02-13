"""Problem 2
Find the sum of the even-valued Fibonacci numbers less than 4 million"""
import numpy as np
import time

def solution1():
    # Find sum of even Fibonacci numbers less than 4 million
    a = 1
    b = 2

    fib_num = a + b   # First new Fibonacci number
    even_fib_nums = 2   # First even number will be 2
    
    while fib_num + a < 4e6:
        fib_num = a + b   # New Fibonacci number

        # Add even fibonacci numbers
        if fib_num % 2 == 0:
            even_fib_nums += fib_num
        
        # Update Fibonacci numbers
        a = b
        b = fib_num
    
    return even_fib_nums


if __name__=='__main__':
    print(solution1())

    
