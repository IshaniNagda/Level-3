class Solution:
    def isIdentical(self,root1, root2):
        a= root1
        b= root2
        if a is None and b is None:
            return True
 
        if a is not None and b is not None:
            return ((a.data == b.data) and
                self.isIdentical(a.left, b.left)and
                self.isIdentical(a.right, b.right))
     
        return False
