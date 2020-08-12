def isPalindrome(head: ListNode):
    if head is None:  # blank list won't have values and will break loop below
        return True

    # collect all values in original order
    values = []
    while head.next is not None:
        values.append(head.val)
        head = head.next
    values.append(head.val)

    return values == values[::-1]  # compare forward list to backward list

"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false

Example 2:

Input: 1->2->2->1
Output: true
"""