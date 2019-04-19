def my_fun(a):
	sum=0
	for i in str(a):
		sum+=int(i)
	return sum

n = int(input())
l1 = sorted([int(i) for i in input().split(" ")])
l = sorted(l1, key = my_fun)

for i in l:
	print(i, end = ' ')
