# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr = []
        curr = head
        while(curr != None):
            arr.append(curr)
            curr = curr.next
        if(n == len(arr)):
            return head.next
        elif(n == 1):
            arr[-2].next = None
            return head
        curr = arr[-n - 1]
        curr.next = arr[-n + 1]
        return head
        
        
        
            
            
        
        
        