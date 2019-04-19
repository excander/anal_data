left, right = 0, 100000
l = []

for i in range(5):
	wasnt = 1
	for j in range(1,11):
		print('?', left+j*(right-left)//10, flush=True)
	print('+')
	for j in range(1,11):
		a = int(input())
		if (a == 1) and wasnt:
			left = left + (j-1)*10**(4-i)
			right = left + 10**(4-i)
			wasnt = 0
		if j == 10 and wasnt:
			left = left + (j-1)*10**(4-i)
			right = left + 10**(4-i)

	# print(left, right)

print('!', right, flush = True) if wasnt else print('!', left, flush = True)
