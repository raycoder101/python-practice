class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: ListNode) -> ListNode:
    """ Reverses a singly linked list iteratively.
    Args:
        head: The head of the linked list.
    Returns:
        The head of the reversed linked list.
    """
    prev = None
    curr = head

    while curr is not None:
        # Store the next node before changing the current node's next pointer
        next_node = curr.next
        
        # Reverse the current node's next pointer to point to the previous node
        curr.next = prev
        
        # Move the pointers one step forward
        prev = curr
        curr = next_node
        
    # After the loop, 'prev' will be the new head of the reversed list
    return prev

# Example Usage:
# Create an original linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

# Function to print the linked list (for verification)
def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

print("Original Linked List:")
print_list(head)

# Reverse the linked list
reversed_head = reverseList(head)

print("Reversed Linked List:")
print_list(reversed_head)

# Example usage:
# Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print(head.val)