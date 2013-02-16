from toolbox import Prime

def main(n):
	limit = (2 * ((n + 1)**2)) - 1
	p = Prime()
	primes = p.sieve(limit)
	d = {
		x:True for x in primes
	}
	res = []
	for i in range(2, n + 1):
		t = (2 * (i**2)) - 1
		if t in d:
			res.append(t)
	return len(res)

if __name__=="__main__":
	print(main(50000000))