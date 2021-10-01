class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists):
        self.ans = []
        head = value = ListNode(0)
        for l in lists:
            while l:
                self.ans.append(l.val)
                l = l.next
            print(self.ans)
        for x in sorted(self.ans):
            value.next = ListNode(x)
            value = value.next
        return head.next

lists = [[1,4,5],[1,3,4],[2,6]]
ans = Solution()
ans.mergeKLists(lists)

# output = [1,1,2,3,4,4,5,6]
#1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6

        