#problem: Given an unsorted integer array, find the smallest missing positive integer.
#shoudl run in O(n)

#questions:
#negatives?
#what happens if theyre all the same number
#no other data types?
#what shoul it return in a list of all negatives
#default return value

#assumptions:


def firstMissingPositive(nums):
        nums = sorted(nums)     #sort numbers in ascending order
        smallest = 1            #the curretn smallest missing positive
        #loop through the list
        for x in range(len(nums)):
            #check if the current number is a positive
            if nums[x] > 0:
                #check to see if its smaller than or equal to the current smallest positive
                if nums[x]<=smallest:
                    #skips duplicates
                    if len(nums)>1 and nums[x] == nums[x-1] and x!=0:
                        continue
                    smallest+=1       #if so the increase the current missing positive
        return smallest
                

print(firstMissingPositive([1,1]))


#var table:
#nums       | [1,2,0], [0,1,2]
#smallest   | 1, 2
#x          | 0, 1
#nums[x]    | 0, 1