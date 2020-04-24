#problem: Given a list of n numbers, determine if it contains any duplicate numbers.

#questions:
# Are the numbers all the same data type
# Run time limit?
# Is it sorted?
# Return bool or int?

#assumptions:
# Its non sorted
# All ints
# Return a bool

#solution: make a histogram, the moment you have to increase a dictionary entry then its a duplicate (runtiem O(n))

def find_dup(numbers):
	histogram = {}
	for x in numbers:
		if histogram.get(x) == None:
			histogram[x]=1
		else:
			return True
	return False

print(find_dup([0,0,1,2,3,]))
print(find_dup([0,1,2,3]))
