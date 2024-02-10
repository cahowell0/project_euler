"""Problem 1
Find the sum of all the multiples of 3 or 5 below 1000"""
import numpy as np 
import time

def solution1():
    # Sum integers divisible by 3 and 5
    final_sum = sum([i for i in range(1000) if i % 3 == 0 or i % 5 == 0])
    return final_sum

def solution2():
    # Sum integers divisible by 3 and 5
    threes = 3*np.arange(334)
    fives = 5*np.arange(200)

    return sum(set(np.concatenate([threes, fives])))


if __name__=='__main__':
    print(solution1())
    print(solution2())
