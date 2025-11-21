#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prime Number Checker"""

def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True

def get_primes_up_to(n):
    return [i for i in range(2, n + 1) if is_prime(i)]

if __name__ == "__main__":
    number = 29
    
    if is_prime(number):
        print(f"{number} is a prime number!")
    else:
        print(f"{number} is not a prime number.")
    
    primes = get_primes_up_to(number)
    print(f"Prime numbers up to {number}: {primes}")
