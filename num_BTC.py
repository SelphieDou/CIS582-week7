import math

def num_BTC(b):
	circulate = 50
	round = b // 210000
	print(round)
	extra = b % 210000
	total = 0
	while round > 0:
		total += 210000 * circulate
		round = round - 1
		circulate = circulate / 2
	total += circulate * extra
	c = float(total)
	return c


