#problem: Given a string of text and a number k, 
# find the k words in the given text that appear most frequently. 
# Return the words in a new array sorted in decreasing order.

#questions:
#is it case sensitive?
#run time limit?
#does the return array need to include the number of times they appear

#assumptions:
#the returning list is made of tuples (the latter and number of times it shows up)
#not case sensitive

#solutions: create a histogram out of the text and then lop througn the histogram to find the top k frequent letters 
# run time O(n)

def letter_frequency(text, k):
    histogram = {}
    for letter in text:
        if histogram[letter] != None:
            histogram[letter]+=1
        else:
            histogram[letter] = 1
    frequent = [] #list of tuples
    if k > len(histogram):
        return None
    for key, num in histogram:
        if len(frequent)==0:
            frequent.append((key, num))
        else:
            if num >= frequent[0]:
                frequent.insert(0, (key, num))
            else:
                frequent.append((key, num))

        if len(frequent) > k:
            del frequent[len(frequent)-1]

            
        