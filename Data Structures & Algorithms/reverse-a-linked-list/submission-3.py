# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return
        prevNode = head
        nextNode = prevNode.next
        prevNode.next = None

        while nextNode != None:
            temp = nextNode.next # hold next pointer
            nextNode.next = prevNode # make the new pointer to the prev node
            prevNode = nextNode # swap the nodes
            nextNode = temp
        return prevNode
            
        