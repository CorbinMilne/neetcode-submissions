# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None or head.next is None:
            return head

        curr = head.next
        prev = head
        temp = curr.next

        prev.next = None

        while curr != None:
            curr.next = prev
            prev = curr
            curr = temp
            if temp is None:
                continue
            else:
                temp = temp.next

        return prev

        
            
            
            

        

        
        