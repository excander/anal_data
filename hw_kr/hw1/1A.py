n = int(input())
ll = input().split(" ")
l = []
k = 0
for c in ll:
	if c not in l:
		l.append(c)
	else:
		k+=1

for i in l:
	print(i, end = ' ')
print()
print(k)