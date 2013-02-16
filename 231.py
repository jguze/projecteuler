import toolbox

def main(n,k):
	prime = toolbox.Prime()
	return sum(prime._find_divisors(2.0876550259138430151321958621352313737634051 * (10**4884377)))


if __name__=="__main__":
	print(main(20000000, 15000000))