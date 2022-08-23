#LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
def lesser_of_two_evens(a,b):
	if (a%2 == 0 and b%2==0):
		if a < b:
			result = a
		else:
			result = b
	else:
		if a > b:
			result = a
		else:
			result = b
	return result

a = 2
b = 4
b = 5


result = lesser_of_two_evens(a,b)
print(result)