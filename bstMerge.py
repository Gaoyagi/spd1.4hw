#problem: You need to merge t2 trees into a new binary tree. 
# The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. 
# Otherwise, the NOT null node will be used as the node of new tree.


#questions:
#run time limit?
#are all the data the same data type
#what do i return? the root node for the new tree?
#where is the new tree stored

#assumptions:
#all the data types are ints
#new tree will replace t1's tree

#solution:
#go throught he tree in pre order traversaland edit the nodes of t1 to reflect the sum of the 2 2 tree nodes

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1==None:
            return t2
        if t2==None:
            return t1

        t1.val += t2.val

        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTree(t1.right, t2.right)
        return t1

    
