#单节点链表
'''class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 申请两个节点，pre和 cur，pre指向None
        pre = None
        cur = head
        # 遍历链表，while循环里面的内容其实可以写成一行
        # 这里只做演示，就不搞那么骚气的写法了
        while cur:
            # 记录当前节点的下一个节点
            tmp = cur.next
            # 然后将当前节点指向pre
            cur.next = pre
            # pre和cur节点都前进一位
            pre = cur
            cur = tmp
        return pre

s= Solution()
l = [1, 2, 3, 4, 5]
print(s.reverseList(l))'''
###################################
'''class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
l1 = Node(3)    # 建立链表3->2->1->9->None
    l1.next = Node(2)
    l1.next.next = Node(1)
    l1.next.next.next = Node(9)
    l = reverseList(l1)
    print (l.elem, l.next.elem, l.next.next.elem, l.next.next.next.elem)
'''
###########
class LinkNode:
    def __init__(self, data = None):
        self.data = data
        self.next = None
class LinkList:
    def __init__(self):
        self.head = LinkNode()
        self.head.next = None
class Solution():
    def fanzhuan(self, head):
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre
s= Solution()
l1 = LinkNode(3)
l1.next = LinkNode(2)
l1.next.next = LinkNode(1)
l = s.fanzhuan(l1)
print(l.data)