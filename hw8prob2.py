#problem:You are given two non-empty linked lists representing two non-negative integers. 
#the digits are stored in reverse order and each of their nodes contain a single digit. 
#Add the two numbers and return it as a linked list.

#questions:
#is the data type integers only?
#does the returned linked list have to be reversed as well?

#assumptions
#all postive integers
#answer also has to be reversed


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#extimated runtime: O(n)
def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    a = convertToNum(l1)    #convert first list to a int (O(n) runtime)
    b = convertToNum(l2)    #convert 2nd list to int (O(n) runtime)
    sum = a+b
    convert = str(sum)
    temp = None
    head = None
    #loop that goes through the sum (converted into a string) and stores the values into a linked list (O(n) runtime)
    for x in range(len(convert)-1, -1, -1):
        if temp == None:
            temp = ListNode(int(convert[x]))
            head = temp
        else:
            temp.next = ListNode(int(convert[x]))
            temp = temp.next

    return head

#helper function that converts teh reversed linekd list into a number
#param: list node object
#return: int sum
#estimated run time: O(n)
def convertToNum(node):
    temp = ""
    while node:
        temp = str(node.val) + temp
        node = node.next
    return int(temp)


