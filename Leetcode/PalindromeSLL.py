"""
Implement a function to check if a linked list is a palindrome
"""
from LLSetup import *

def isPalindrome(head: Node) -> bool:
    revLLHead = deepRevSLL(head)

    while head != None:
        if head.data != revLLHead.data:
            return False
        head = head.next
        revLLHead = revLLHead.next
    
    return True

# could use stack

if __name__ == "__main__":
    print(isPalindrome(Node(5, Node(4, Node(3, Node(1, Node(7, Node(1, Node(3, Node(4, Node(5)))))))))))