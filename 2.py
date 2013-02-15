

class A(object):
	def __init__(self):
		self.sum = 0

	def fib(self, a,b):
		if a + b > 4000000:
			return
		if a % 2 == 0:
			self.sum += a
		print a + b
		self.fib(b, a + b)

a = A()
a.fib(1,2)
print 1,2
print a.sum + 