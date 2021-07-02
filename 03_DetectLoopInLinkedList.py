#Floyd's cycle finding algorithm

def detectLoop(self, head):
        fast = head
        slow = head
        while(slow != None and fast != None and fast.next!= None):
            slow = slow.next 
            fast = fast.next.next
            if(slow == fast):
                return True


        return False
