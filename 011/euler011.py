import numpy as np

chainlength = 0

startnumber = 999999
while startnumber > 700000:
	k = 1
	number = startnumber
	while number != 1:
		
		if (number%2):
			number = 3*number + 1
		else:
			number /= 2
		k += 1
	
	if k > chainlength:
		chainlength = k
		print 'chainlength for %s: %s' % (startnumber, k)
	startnumber -= 1

print chainlength