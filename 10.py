import sieve
import sys

def sum_primes(n):
	return sum(sieve.sieve(n))

if __name__ == "__main__":
	print sum_primes(int(sys.argv[1]))