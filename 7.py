class Seven(object):
	def __init__(self):
		self._primes = {2:0,3:0}

	def calculateResult(self):
		result = 1
		for key in self._primes.keys():
			result *= self.calcInd(key, self._primes[key])
		return result

	def calculateInd(self, value, exp):
		result = 1
		for i in range(exp):
			result = result * value
		return result 

	def isprime(self, value):
		for key in self._primes.keys():
			while True:
				result = calculateResult()
				if value > result:
					return True

	def reset():
		for key in _primes.keys():
			self._primes[key] = 0


class Sieve(object):
	def __init__(self,limit, tofind):
		self.nl = [i for i in range(2,limit)]
		self.primes = []
		self.tofind = tofind

	def filter(self,mod):
		for i in self.nl:
			if i % mod == 0:
				self.nl.remove(i)

	def run(self):
		#Get prime
		#filter
		#if prime is amount chosen, win

		while True:
			prime = self.nl[0]
			self.primes.append(prime)
			self.filter(prime)

			if self.tofind == len(self.primes):
				return self.primes[-1]

			if len(self.nl) == 0:
				return "Need a higher limit len:last", len(self.primes), ":", self.primes[-1] 

s = Sieve(250000, 10001)
print s.run()