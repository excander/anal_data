n, k = input().split(" ")
n,k = int(n), int(k)
diff = n - k

l = [1, 2]

if diff % 2 == 0:
	for i in range(diff//2):
		l.append(1)
		l.append(2)
else:
	for i in range(diff//2):
		l.append(1)
		l.append(2)
	l.append(1)

for i in range(3, k+1):
	l.append(i)  

for i in l:
	print(i, end = ' ')
