def square(x):
	return x*x

def sumup(x):
	s = 0
	for i in range(1,x+1):
		s += i
	return s

def sumsquare(x):
	return square(sumup(x))


value = 100
s = 0
for i in range(1,value + 1):
	s += square(i)

print sumsquare(value) - s