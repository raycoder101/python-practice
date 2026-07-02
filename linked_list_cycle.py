class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Example 1: Linked list with a cycle
head_cycle = ListNode(3)
node2 = ListNode(2)
node0 = ListNode(0)
node_minus4 = ListNode(-4)

head_cycle.next = node2
node2.next = node0
node0.next = node_minus4
node_minus4.next = node2  # Creates a cycle pointing back to node2

print('node is ', head_cycle, head_cycle.val, head_cycle.next)
print('node is ', node2, node2.val, node2.next)
print('node is ', node0, node0.val, node0.next)
print('node is ', node_minus4, node_minus4.val, node_minus4.next)

# Example 2: Linked list without a cycle
head_no_cycle = ListNode(1)
head_no_cycle.next = ListNode(2)

print('node is ', head_no_cycle.val, head_no_cycle.next)
print('node is ', head_no_cycle.next.val, head_no_cycle.next.next)

class Solution(object):
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            print(slow, slow.next, fast)

            if slow == fast:
                return True
        return False

"""
    def hasCycle(self, head: ListNode) -> bool:
        seen = []

        while head:
            if head in seen:
                    return True
            seen.append(head)
            head = head.next
        
        return False
"""

solver = Solution()
print(solver.hasCycle(head_cycle))     # Expected: True
print(solver.hasCycle(head_no_cycle))  # Expected: False