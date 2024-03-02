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


def solution2():
    # Find sum of even Fibonacci numbers less than 4 million
    a = 1
    b = 2

    c = a + b   # This will be odd, so we don't want to include it
    d = c + c + b   # Even term, so include this one in the final sum
    fib_num_sum = b + d

    while True:
        fib_num = 2*(d + c + b) + d   # This skips two Fibonacci numbers, essentiall ignoring the odds
        
        if fib_num < 2e6:
            fib_num_sum += fib_num   # Update sum of even Fibonacci numbers
            break

        # Update Fibonacci numbers, skipping the odd terms
        c = d + c + b
        b = d
        d = fib_num

    return fib_num_sum

if __name__=='__main__':
    time1 = time.perf_counter()
    print(solution1())
    time2 = time.perf_counter()
    print(solution2())
    time3 = time.perf_counter()

    print(time2 - time1)
    print(time3 - time2)

    
