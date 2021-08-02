def getNthFromLast(head,n):
    temp = head
    slow=fast=head
    count=1
    while temp.next is not None:
        count+=1
        temp=temp.next
    
    if n>count:
        return -1
    
    else:
        while(n!=0):
            fast=fast.next
            n-=1
        
        while(fast):
            slow=slow.next
            fast=fast.next
        
        return slow.data
