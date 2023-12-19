#https://leetcode.com/problems/merge-k-sorted-lists/
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        he = []
        for each_root in lists:
            while each_root is not None:
                #print(each_root)
                heapq.heappush(he,each_root.val)
                each_root=each_root.next
        head = None
        tail = None
        while he:
            ans=heapq.heappop(he)
            currNode = ListNode(ans)
            #appending data to a new list
            if head is None:
                head=tail=currNode
            else:
                tail.next=currNode
                tail = tail.next
        return head