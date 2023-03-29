# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Set two pointers, slow and fast, starting from the head of the linked list
        slow = head
        fast = head

        # Move the fast pointer two steps ahead and the slow pointer one step ahead until the end of the linked list
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the linked list
        revHeadf = slow.next
        slow.next = None
        head2 = self.reverse(revHeadf)

        # Merge the first half and reversed second half of the linked list
        self.merge(head, head2)

        # Return the head of the reordered linked list
        return head

    def reverse(self, revHead):
       # Set the previous node to None and the current node to the head of the linked list to be reversed
        prev = None
        curr = revHead
        # Traverse the linked list and reverse the pointers
        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # Return the new head of the reversed linked list
        return prev

    def merge(self, head, head2):
        # Traverse both linked lists and merge them
        while head2:
            temp = head.next
            head.next = head2
            head2 = head2.next
            head.next.next = temp
            head = temp

#TC - O(N)
#SC - O(1)
