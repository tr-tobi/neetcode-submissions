# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        current_node = head

        while current_node:
            arr.append(current_node.val)
            current_node = current_node.next
        if len(arr) == 0:
            return head
        reverse_head = ListNode(arr.pop())
        current_reverse = reverse_head
        while arr:
            current_reverse.next = ListNode(arr.pop())
            current_reverse = current_reverse.next
        return reverse_head
