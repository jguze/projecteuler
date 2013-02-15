from toolbox import Prime

def triangles():
	i = 3
	count = 3
	while True:
		prime = Prime()
		prime_factors = prime.factor(i)
		mul = 1;
		for key, amount in prime_factors.items():
			mul *= (amount + 1)
		if mul > 500:
		 	return i
		i += count
		count += 1

if __name__=="__main__":
	print(triangles())