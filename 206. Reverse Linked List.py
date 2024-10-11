# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # works first time after years of not practicing linked list, but not as elegant
        # if not head:
        #     return None

        # prev = None
        # curr = head
        # next_node = head.next
        # rev = curr
        # rev.next = prev
        # prev = curr

        # while next_node!=None:
        #     curr = next_node
        #     next_node = next_node.next
        #     rev = curr
        #     rev.next = prev
        #     prev = curr

        # return rev

        rev = None

        while head:
            rev, head.next, head = head, rev, head.next

        return rev