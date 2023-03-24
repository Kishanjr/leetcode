# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# TC - is O(n) . we travese each node of the linked list atleast once
# SC - is O(1)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # create  pointers to keep track of previous and current nodes
        prev = None
        current = head

        # Traverse the linked list and reverse the direction of each node's next pointer
        while current != None:
            current.next, prev, current = prev, current, current.next

        # The new head of the reversed list is the last node in the original list, which is now the first node in the reversed list
        return prev
