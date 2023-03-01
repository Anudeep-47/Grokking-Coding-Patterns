'''

Given the head of a singly linked list, 
reverse the linked list and return its updated head.

'''


from linked_list import LinkedList
from print_list import print_list_with_forward_arrow


def reverse(head):
    if head is None:
        return head
    prev = None
    cur = head
    while cur:
        temp = cur.next
        cur.next = prev
        prev, cur = cur, temp

    return prev


def main():
    print('')
    input_list = [1, 2, 3, 4, 5, 6, 7]
    input_linked_list = LinkedList()
    input_linked_list.create_linked_list(input_list)

    print("The original linked list:  ", end='')
    print_list_with_forward_arrow(input_linked_list.head)
    result = reverse(input_linked_list.head)
    print("\n\nThe reversed linked list:  ", sep='', end='')
    print_list_with_forward_arrow(result)


if __name__ == '__main__':
    main()