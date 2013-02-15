if __name__=="__main__":
	f = open("13_input.txt")
	summation = 0
	for line in f:
		summation += int(line)
	print summation