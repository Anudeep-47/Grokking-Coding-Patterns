'''

Given a linked list, 
reverse the nodes of the linked list k at a time and return the modified list. 
Here, k is a positive integer and is less than or equal to the length of the linked list. 
If the number of nodes is not a multiple of k, 
the nodes left in the end will remain in their original order.

You can't alter the values of the linked list nodes. 
Only the nodes themselves may be changed.

Note: Use only O(1) extra memory space.

'''


from __future__ import print_function
from linked_list import LinkedList
from print_list import print_list_with_forward_arrow


# reverse will reverse the k number of nodes in the linked list
def reverse_k(head, k):
    prev, cur = None, head
    while cur and k>0:
        temp = cur.next
        cur.next = prev
        prev, cur = cur, temp
        k -= 1
    return prev, cur


# find_length will find the total length of the linked list
def find_length(start):
    count = 0
    while start:
        start = start.next
        count += 1
    return count


# reverse_linked_list is our challenge function that will reverse
# the group of k nodes in the linked list
def reverse_linked_list(head, k):
    if head is None or k<=1:
        return head
    list_len = find_length(head)
    groups = list_len//k
    prev, cur = None, head
    while groups>0:
        prev_last_node = prev
        cur_last_node = cur
        prev, cur = reverse_k(cur, k)
        if prev_last_node:
            prev_last_node.next = prev
        else:
            head = prev
        prev = cur_last_node
        prev.next = cur
        groups -= 1
    return head


def main():
    print('')
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    input_linked_list = LinkedList()
    input_linked_list.create_linked_list(input_list)

    print("The original linked list: ", end='')
    print_list_with_forward_arrow(input_linked_list.head)
    result = reverse_linked_list(input_linked_list.head, 2)
    print("\n\nReversed linked list, with k = ", 2, ": ", sep='', end='')
    print_list_with_forward_arrow(result)


if __name__ == '__main__':
    main()