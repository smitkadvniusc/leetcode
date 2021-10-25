#https://leetcode.com/problems/sum-of-left-leaves/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root == None :
            return 0
        ls = []
        temp = root
        ls.append([temp,"root"])
        ret = 0
        while len(ls) != 0:
            temp,pos = ls.pop()
            if temp.left == None and temp.right == None:
                print(temp.val)
                if pos == "left":
                    ret += temp.val
            else:
                if temp.left != None:
                    ls.append([temp.left,"left"])
                if temp.right != None:
                    ls.append([temp.right,"right"])
        return ret
                
              

