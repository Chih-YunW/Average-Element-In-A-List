def avg(n):
	sum = 0
	for t in n:
		sum = sum + t
	if len(n) == 0:
		return 0
	else:
		avg = sum / len(n)
		return avg

