# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr_1 = l1
        curr_2 = l2
        str_1 = ""
        str_2 = ""
        
        while (curr_1 is not None):
            str_1 = str(curr_1.val) + str_1
            curr_1 = curr_1.next
        while (curr_2 is not None):
            str_2 = str(curr_2.val) + str_2
            curr_2 = curr_2.next
        res = int(str_1) + int(str_2)
        
        result_str = str(res)[::-1]  # Reverse the string
        
        # Create a dummy node to simplify the linked list creation
        dummy = ListNode(0)
        curr = dummy
        
        for digit in result_str:
            curr.next = ListNode(int(digit))
            curr = curr.next
        
        return dummy.next
            
    
        
        