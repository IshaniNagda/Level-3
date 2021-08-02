#the head pointer is not given
#only the pointer to the node to be deleted is given

def deleteNode(self,curr_node):
        #code here
        temp=curr_node.next
        curr_node.data= temp.data
        curr_node.next=temp.next
