"""Problem 1
Find the sum of all the multiples of 3 or 5 below 1000"""

def sum_fizz_buzz_multiples(a=3, b=5, n=1000):
    # Sum integers divisible by 3 and 5
    final_sum = sum([i if i % a == 0 or i % b == 0 else 0 for i in range(n)])
    return final_sum


if __name__=='__main__':
    print(sum_fizz_buzz_multiples())
