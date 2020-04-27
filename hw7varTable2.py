#problem: Given a non-empty array of integers, every element appears twice except for one. Find that single one.
#linear run time

#questions:
#sorted or unsorted?
#theres no other data types?
#are the instances of more than 1 repeat
#negative numbers?

#assumptions:
#unsorted
#all ints
#theres only 1 repeat per number

def find_single(numbers):
    numbers = sorted(numbers)    #1 loop, O(n)
    for x in range(0, len(numbers), 2):
        if x == len(numbers)-1:
            return numbers[x]
        elif numbers[x] != numbers[x+1]:
            return numbers[x]

    return None

print(find_single([4,1,2,2,1]))


#var table
# numbers   | [4,1,2,2,], [1,1,2,2,4]
# x         | 0,2,4
# numbers[x]| 1,2,4