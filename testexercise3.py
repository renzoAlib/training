#MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
def makes_twenty(n1,n2):
#one line answer
	return (n1+n2) == 20 or n1==20 or n2==20
	
#must be an elif/s on each arg not "or"
	"""if (n1+n2) == 20 or #elif n1==20 or #elifn2==20
		return True
	else:
		return False"""
n1 = 20
n2 = 10
num = makes_twenty(n1,n2)
print(num)
