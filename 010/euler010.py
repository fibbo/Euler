import numpy as np

numbers = np.loadtxt('numbers')

total_sum = 0
for number in numbers:
	total_sum += number

strsum = str(total_sum)

for i in range(11):
	print strsum[i]