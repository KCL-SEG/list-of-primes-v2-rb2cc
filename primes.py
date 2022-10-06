import re


"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""


def isPrime(n):
    # Use regex function to find n primes.
    return re.match(r'^1?$|^(11+?)\1+$', '1' * n) == None


def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError("mexssage")

    else:
        list = []

        while len(list) < number_of_primes:
            upper = 100
            # Add n primes to our list.
            list += filter(isPrime, range(upper - 100, upper))
            upper += 100

        # Cap the number of primes shown to "number_of_primes"
        return list[:number_of_primes]
