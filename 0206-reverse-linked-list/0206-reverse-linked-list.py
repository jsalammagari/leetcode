# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.helper(None,head)
    def helper(self,previous,current):
        if current == None:
            return previous
        next_node = current.next
        current.next = previous
        return self.helper(current,next_node)