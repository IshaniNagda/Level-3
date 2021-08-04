def removeDuplicates(head):
    temp= head
    if temp is None:
        return temp
    
    while temp.next:
        if temp.data== temp.next.data:
            temp.next=temp.next.next
        
        else:
            temp=temp.next
    
    return head
