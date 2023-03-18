# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# TC - is O(n) .
# SC - is O(1)

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize two pointers, slow and fast, to the head of the linked list
        slow = head
        fast = head

        # creat  a variable to keep track of whether a cycle has been detected
        cycle = False

        # Traverse the linked list with the two pointers, moving the slow pointer one step and the fast pointer two steps at a time
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

            # If the pointers meet at the same node, a cycle has been detected
            if slow == fast:
                cycle = True
                break

        # If a cycle has been detected, reset the slow pointer to the head of the linked list and traverse the list again with both pointers one step at a time
        if cycle:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next

            # The node where the two pointers meet is the starting node of the cycle
            return slow

        # If no cycle has been detected, return None
        return None
