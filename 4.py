def has_palindrome(value):
	val = str(value)
	i = 0
	for i in range(len(val)):
		if val[i] != val[-1 * (i + 1)]:
			return False
	return True

l = []
j = 999
while j > 0:
	k = j
	while k > 0:
		if has_palindrome(j*k):
			l.append((j,k))
		k-=1
	j-=1

large = (0,0)
for s in l:
	if s[0] * s[1] > large[0] * large[1]:
		large = s
print large