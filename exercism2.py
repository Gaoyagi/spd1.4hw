#problem: Determine if a sentence is a pangram. 
# A pangram (Greek: παν γράμμα, pan gramma, "every letter") is a sentence using every letter of the alphabet at least once. 

#questions:
#is it case sensitive?
#time complexity limit?

#assumptions:
#not case senstive

def is_panagram(sentence):
    count = {}
    for letter in sentence:
        l = letter.lower()  #convert to lowercase
        #check to see if character is a letter
        if l.isalpha():     
            #adds it to the count if it is a letter
            if count.get(l) == None:
                count[l] = 0
            else:
                count[l]+=1
    #check to see if the length of count is 26
    if len(count) == 26:
        return True
    else: 
        return False

assert is_panagram("The quick brown fox jumps over the lazy dog") == True
assert is_panagram("absdfdsav") == False
