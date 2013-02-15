import math

def sieve1(n):
    """
    Finds all the prime numbers from 1 to n using
    the Sieve of Atkins.
    Returns a list of primes.
    """
    limit = int(math.sqrt(n)) + 1
    sieve_dict = {
        i:False for i in range(5,n)
    }
    sieve_dict[2] = True
    sieve_dict[3] = True
    sieve_dict[5] = True

    for x in range(1,limit):
        for y in range(1,limit):
            x_square = x*x
            y_square = y*y
            val = (4 * x_square) + y_square
            if (val <= n) and (val % 12 == 1 or n % 12 == 5):
                sieve_dict[val] = not sieve_dict[val]
            val = (3 * x_square) + y_square
            if (val <= n) and (val % 12 == 7):
                sieve_dict[val] = not sieve_dict[val]
            val = (3 * x_square) - y_square
            if (x > y) and (val <= n) and (val % 12 == 11):
                sieve_dict[val] = not sieve_dict[val]

    for k in range(5,limit):
        if sieve_dict[k]:
            i = 1
            square_prime_mul = i * (k * k)
            while  square_prime_mul < n + 1:
                sieve_dict[square_prime_mul] = False
                i += 1
                square_prime_mul = i * (k * k)
    return [prime for prime, value in sieve_dict.items() if value]

def sieve(n):
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