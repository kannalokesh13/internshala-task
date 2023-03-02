class Solution:
    def IsCircular(head,pos):
        if(head==None or head.next==None):
            return True
   
        slow=head
        fast=head

        while(fast.next!=None and fast.next.next!=None):
            fast=fast.next.next
            slow=slow.next
            if(fast==slow):
                return True
        else:
            return False
