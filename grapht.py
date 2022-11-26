# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
         
class Solution:
    def are_symetric(self,root1,root2):
        if root1 is None and root2 is None:
            return True
        elif ((root1 is None) != (root2 is None)) or root1.val != root2.val:
            return False
        else:
            return self.are_symetric(root1.left,root2.right) and self.are_symetric(root1.right,root2.left)    
        
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.are_symetric(root.left,root.right)
      
        
        
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(2)
d = TreeNode(3)
e = TreeNode(4)
f = TreeNode(4)
q = TreeNode(3)
a.left = b # 2
a.right = c # 2

b.left = d # 3
b.right = e# 4
c.left = f # 4
c.right = q# 

re = Solution()
te = re.isSymmetric(a)
print(te)
        

