class ListNode:
     def __init__(self, x, next = None):
         self.val = x
         self.next = next

class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        
        if l1.val <= l2.val:
            Pptr = l1.next
            cpyPtr = l1
            Sptr = l2
            BSPtr = l2
        else:
            Pptr = l2.next
            cpyPtr = l2
            Sptr = l1
            BSPtr = l1
        
        retVal = cpyPtr
            
        while Pptr != None and Sptr != None:
            if Pptr.val <= Sptr.val:
                cpyPtr = cpyPtr.next
                Pptr = Pptr.next
            else:
                BSPtr = Sptr.next
                cpyPtr.next = Sptr
                Sptr.next = Pptr
                cpyPtr = cpyPtr.next
                Sptr = BSPtr
        
        if Pptr is None:
            cpyPtr.next = Sptr
            
        return retVal

if __name__ == "__main__":
    #[-10,-9,-6,-4,1,9,9]
    #[-5,-3,0,7,8,8]

    l1 = ListNode(-10, ListNode(-9,ListNode(-6,ListNode(-4,ListNode(1,ListNode(9,ListNode(9)))))))
    l2 = ListNode(-5,ListNode(-3,ListNode(0,ListNode(7,ListNode(8,ListNode(8))))))
    sol = Solution()
    print(sol.mergeTwoLists(l1,l2)) 


        