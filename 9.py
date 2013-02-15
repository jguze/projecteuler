import math

def pythag():
	for i in range(1,1000):
		for j in range(1,1000):
			res = math.sqrt(i*i + j*j)
			if  i + j + res == 1000:
				return int(i*j*res)

if __name__=="__main__":
	print pythag()