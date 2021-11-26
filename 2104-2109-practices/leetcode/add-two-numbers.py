"""
ListNode1 -> ListNode2 -> ListNode3 ... : next로 이어진 것
next를 먼저 할당하고, next를 curr로 업데이트해야
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        added = ListNode(val=(l1.val + l2.val) % 10)
        carry = (l1.val + l2.val) // 10
        curr = added

        # l1, l2 next -> l1, l2 업데이트, curr next -> curr 업데이트
        while l1.next and l2.next:
            l1 = l1.next
            l2 = l2.next

            curr.next = ListNode(val=(carry + l1.val + l2.val) % 10)
            carry = (carry + l1.val + l2.val) // 10
            curr = curr.next

        # l1.next만 있을 때
        while l1.next:
            l1 = l1.next
            curr.next = ListNode(val=(carry + l1.val) % 10)
            carry = (carry + l1.val) // 10
            curr = curr.next

        # l2.next만 있을 때
        while l2.next:
            l2 = l2.next
            curr.next = ListNode(val=(carry + l2.val) % 10)
            carry = (carry + l2.val) // 10
            curr = curr.next

        # 맨 앞자리 carry 존재 시
        if carry > 0:
            curr.next = ListNode(val=carry)

        return added