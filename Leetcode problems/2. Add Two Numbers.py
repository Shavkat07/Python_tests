from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        return [int(i) for i in  str(int(''.join([str(i) for i in l1[::-1]])) + int(''.join([str(i) for i in l2[::-1]])))[::-1]]



s = Solution()
# l1 = ListNode()
# l1.val = [2, 4, 3]
# l1.next = [5, 6, 4]
print(s.addTwoNumbers(l1=[2, 4, 3], l2=[5, 6, 4]))
