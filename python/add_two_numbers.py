# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        result = None

        while not (l1 is None and l2 is None):
            val1 = 0
            val2 = 0

            if l1 is not None:
                val1 = l1.val
                l1 = l1.next

            if l2 is not None:
                val2 = l2.val
                l2 = l2.next

            sum_ = val1 + val2 + carry
            carry = sum_ // 10
            sum_ = sum_ % 10

            sum_node = ListNode(sum_)

            if result is None:
                result = trav = sum_node
            else:
                trav.next = sum_node
                trav = trav.next

        if carry:
            trav.next = ListNode(carry)

        return result

# test here
def create_list_node(nums: list) -> ListNode:
    list_node = None

    for v in nums:
        if list_node is None:
            list_node = trav = ListNode(v)
        else:
            trav.next = ListNode(v)
            trav = trav.next

    return list_node

list1 = create_list_node([9] * 7)
list2 = create_list_node([9] * 4)

list3 = Solution().addTwoNumbers(list1, list2)

trav = list3

print('[', end='')
while trav:
    print(trav.val, end=', ')
    trav = trav.next
print(']')
