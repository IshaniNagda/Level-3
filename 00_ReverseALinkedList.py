class Solution:
    #Function to reverse a linked list.
    def reverseList(self, head):
        prev= None
        current= head
        while(current!=None):
            after= current.next
            current.next=prev
            
            prev=current
            current=after
        head=prev
        return head
