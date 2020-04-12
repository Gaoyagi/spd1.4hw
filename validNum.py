#problem: Validate if a given string can be interpreted as a decimal number.

#questions:
#is there a run time requirement
#does case matter?
#what does a vald number with e look like?
#what if theres spaces between valid numbers?
#can you chain positives and negative signs?
#do positive signs count?
#do equations count
#you can do exponents of exponents?
#decimals are allowed in both exponents and the base number?
#can you have a leading decimal?

#assumptions:
#case senstive for e
#spaces invalidate the number if not trailing or leading
#cannot chain positive and negative signs, con only do one
#equations dont count
#you cant do exponents of exponents?
#decimals cant exist in the exponent component
#

#solution:
#im going to loop over the string and check if the character is a number, e, or a negative signs
#if the character is a number then its added to the base variable
#if it finds e, then it adds the subsequent numbers to exponent variable

def isNumber(s):
    text = s.strip()        #strips the leading and trailing spaces
    exponent = ""
    base = ""
    expHasNone = False
    baseHasNum = False         #indicates if the base or exponent has numbers
    isExponent = False     #indciates if you're looking at numbers for the exponent or not
    decimal = False        #indicates if you're looking numbers for the base
    for num in text:
        #if it finds the exponent symbol but no base number has been found
        if num == 'e':
            #exponent cant be the first item in the number
            if len(base) == 0: 
                print("exponents cant begin your number")
                return False
            #you cant have 2 exponents in the same num
            elif isExponent == True:
                print("can't have 2 exponents in 1 number")
                return False
            #you cant end with e
            elif num == text[len(text)-1]:
                return False
            else:
                isExponent = True
                decimal = True  #when you start analyzing exponents, you become allwoed to have decimals again
                hasNum = False  #the hasNum now keeps tracks if the exponent has numbers
        #if the character is number
        elif num.isnumeric():
            #if e was mentioned previously it means this is an exponent number
            if isExponent:
                exponent+=num
                expHasNum = True
            else:
                base+=num
                baseHasNum = True
        #if the chracter is a + or - ign
        elif num == '-' or num == '+':
            #a sign cant be the last number
            if num == text[len(text)-1]:
                return False
            #check to see if they're prefacing any number, if they arent then its False
            if isExponent:
                if len(exponent)==0:
                    exponent+=num
                else:
                    print("a exponent number can't have 2 signs")
                    return False
            else:
                if len(base) == 0:
                    base+=num
                else:
                    print("base number can't have 2 signs")
                    return False
        #if the character is a decimal
        elif num == '.':
            #you cant have 2 decimals in 1 number
            if decimal == True:
                print("a number cant have 2 decimals")
                return False
            else:
                if isExponent:
                    exponent+=num
                    decimal = True
                else:
                    base+=num
                    decimal = True
        #if the character is a space
        elif num == " ":
            #you cant have spaces in an already existing number
            if len(base)>0 or len(exponent)>0:
                print("numbers dont have spaces in them")
                return False
        else:
            return False
    if baseHasNum:
        return True
    else:
        return False


print(isNumber(".e1"))