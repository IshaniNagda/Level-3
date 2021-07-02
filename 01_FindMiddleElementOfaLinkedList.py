def findMid(head):
    if (head==None):
        return -1
    else:
        slow=head
        fast=head

        while(slow.next!=None and fast.next!=None):
            slow=slow.next
            fast=fast.next
            if fast.next:
                fast=fast.next
    
        return slow.data
