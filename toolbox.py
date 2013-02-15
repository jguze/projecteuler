import math
from collections import Counter

class Prime(object):
    """
    All prime related will be placed in this object
    for later use
    """
    def __init__(self):
        self._divisor = {
            1: [],
            2: [2],
            3: [3],
            4: [2,2],
            5: [5],
            6: [2,3],
            7: [7]
        }

    def factor(self, n):
        """
        Find the prime factors of a number. Returns
        a collections.Counter object with prime:amount as
        the key:value pair
        """
        return Counter(self._find_divisors(n))

    def _find_divisors(self, n):
        """
        Given a number n, it will return a list of all
        prime numbers that divide it. Will return duplicates
        """
        if n in self._divisor:
            return self._divisor[n]
        
        i = 2
        # if it's not even, why bother checking if divisible by evens
        if n & 1 == 1:
            i = 3

        divs_list = []
        while n % i != 0:
            i += 2
        divs_list.append(i)
        divs_list = divs_list + self._find_divisors(n/i)
        self._divisor[n] = divs_list
        n /= i
        return divs_list

    def sieve(self, n):
        """
        This is implemented using Atkins sieve to be very fast,
        and was not written by me
        http://stackoverflow.com/a/3035188
        """
        sieve_list = [True] * n
        for i in xrange(3,int(n**0.5)+1,2):
            if sieve_list[i]:
                sieve_list[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
        return [2] + [i for i in xrange(3,n,2) if sieve_list[i]]
