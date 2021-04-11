nner(self, n: int, k: int) -> int:
        
        # construct a double linked list node class
        class DoubleLinkedListNode:
            def __init__(self, val):
                self.val = val
                self.prev = None
                self.next = None
        
        # step-1: construct the circular double linked list
        head = DoubleLinkedListNode(1)
        curr = head
        for i in range(2,n+1):
            new_curr = DoubleLinkedListNode(i)
            new_curr.prev = curr
            curr.next = new_curr
            curr = new_curr
        curr.next = head
        head.prev = curr
            
        
        # step-2: do the loop ( check if the size is 1, if not, find the k-th element and delete)
        curr = head
        while curr.next != curr:
            for _ in range(k-1):
                curr = curr.next
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            curr = curr.next
        
        
        # step-3: return the result
        return curr.val
                
        
