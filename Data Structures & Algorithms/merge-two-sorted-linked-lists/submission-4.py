# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1:
            return list2
        if not list2:
            return list1

        result = ListNode(0)
        if list1.val < list2.val:
            result.next = list1
            curr1, curr2 = list1.next, list2
        else:
            result.next = list2
            curr1, curr2 = list1, list2.next

        prev = result.next
        temp = None

        while curr1 and curr2:

            if curr1.val == curr2.val:
                temp = curr1.next
                curr1.next = curr2
                prev.next = curr1
                curr1 = temp
                prev = curr2
                curr2 = curr2.next

            elif curr1.val < curr2.val:
                temp = curr1.next
                prev.next = curr1
                prev = curr1
                curr1.next = curr2
                curr1 = temp

            else:
                temp = curr2.next
                prev.next = curr2
                prev = curr2
                curr2.next = curr1
                curr2 = temp

        if curr1:
            prev.next = curr1
        else:
            prev.next = curr2

        return result.next  
        

