def t(n):
	if n & 1 == 1:
		return (3 * n) + 1
	else:
		return n / 2

def main():
	#This could be way better if I did it recursively
	known = { # value, length
		1:1,
		13:10,
		40:9,
		20:8,
		10:7,
		5:6,
		16:5,
		8:4,
		4:3,
		2:2
	}
	maximum = (1,1) # starting number, length
	for i in range(2,1000000):
		length = 0
		n = i
		while n != 1:
			if n in known:
				length += known[n]
				break
			else:
				length += 1
				n = t(n)
		known[i] = length
		if length > maximum[1]:
			maximum = (i, length)
	return maximum[0]

if __name__=="__main__":
	print(main())