from toolbox import Prime
def largest_prime_factor(n):
	prime = Prime()
	return max(prime.factor(n).keys())

if __name__=="__main__":
	print(largest_prime_factor(600851475143))