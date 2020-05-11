#problem: Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
#Find all unique triplets in the array which gives the sum of zero.

#questions:
#time compelxity limit?
#are they ordered?
#what happens if none of the numbers add up to 0
#can the unique set of 3 numbers contain overlapping numbers
#

#assumptions:
# all integers 
# no time complexity limit
#not sorted

#estimated runtime  is techincally O(n^2) despite there being 2 O(n^2) solutions (still too slow to be accepted :P)
def threeSum(nums):
    triples = []          #list of list to hold the unique triplets
    nums = sorted(nums)   #sorts it list ascending order  (O(n) runtime)
    
    x = 0
    #loops through the entire list but have two other counters loop through the list in a single run (O(n^2) runtime)
    while x<len(nums):
        right = len(nums)-1
        left = x+1
        while left<right:
            #if the right or left counters match x, then skip that number
            if left == x:
                left+=1
                continue
            elif right == x:
                right-=1
                continue

            #check the sum of the numbers at the 3 counters
            #if they equal 0, append to triples
            if nums[x]+nums[left]+nums[right] == 0:
                temp = [nums[x], nums[left], nums[right]]
                temp.sort()
                triples.append(temp)     
                left+=1
                right-=1    
            #if sum too small, then left is too small and should be increased
            elif nums[x]+nums[left]+nums[right] < 0:
                left+=1
            #if sum too big, then right is too big and should be decreased
            else:
                right-=1
        x+=1

    x = 0
    #loop through the triples to find any duplicate elements (extimate runtime O(n^2))
    while x < len(triples):
        y=x+1
        while y < len(triples):
            if triples[y] == triples[x]:
                del triples[y]
            else:
                y+=1    
        x+=1

    return triples

print(threeSum([-1,0,1,2,-1,-4]))

