class Solution:
    def isPalindrome(self, head):
        arr=[]
        temp=head
        while(temp!=None):
            arr.append(temp.data)
            temp=temp.next
        j=len(arr)-1
        i=0
        while(i<j):
            if arr[i]!=arr[j]:
                return 0
            i+=1
            j-=1
        return 1
