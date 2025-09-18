"""
Write a script that lists all the prime numbers between 1 and 10000.
(A prime number is an integer greater or equal to 2 which has no divisors except 1 and itself). 
Hint: Write an is_factor helper function.
"""

def is_factor(d, n):
    """True iff (if and only if) d is a divisor of n."""
    return n % d == 0

def is_prime(n):
    """Return True if n is a prime number, False otherwise."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:  
        return False
    

    for i in range(3, int(n**0.5) + 1, 2):
        if is_factor(i, n):
            return False
    return True


list_of_primes = []
for num in range(1, 10001):
    if is_prime(num):
        list_of_primes.append(num)

print(list_of_primes)
