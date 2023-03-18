# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# TC - is O(n) .
# SC - is O(1)

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Initialize two pointers, slow and fast, to the head of the linked list
        slow = head
        fast = head

        # Traverse the linked list with the fast pointer, moving it n steps ahead of the slow pointer
        while n:
            if fast.next != None:
                fast = fast.next
                n -= 1
            else:
                # If n is greater than the length of the list, remove the head node and return the next node
                return head.next

        # Traverse the linked list with both pointers until the fast pointer reaches last
        while fast.next != None:
            slow = slow.next
            fast = fast.next

        # The slow pointer is now at the (n-1)th node from the end of the list. Remove the nth node by updating the next pointer of the (n-1)th node.
        slow.next = slow.next.next

        # Return the head of the modified linked list
        return head
