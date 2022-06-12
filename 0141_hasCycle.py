class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = next
    
class Solution:
  def hasCycle(self, head):
    if head is None:
      return False
    
    slow = head
    fast = head.next
    
    while slow != fast:
      if fast is None or fast.next is None:
        return False
      slow = slow.next
      fast = fast.next.next
    return True
  
  
  # O(n), O(1)
