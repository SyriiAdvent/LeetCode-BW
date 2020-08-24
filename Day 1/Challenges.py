"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        map = {}

        for i in nums:
            if i in map:
                map[i] += 1
                if map[i] >= 2:
                    return True
            else:
                map[i] = 1

        return False



"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

"""

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1.next is None and l2.next is None:
            if l1.val > l2.val:
                return l1
            else:
                return l2
        
        def getNum(ll):
            temp = []
            node = ll
            while node is not None:
                temp.append(str(node.val))
                node = node.next
            return int("".join(temp))
        
        num = str(getNum(l1) + getNum(l2))
        new_num = list(num)
        
        new_ll = ListNode(new_num[-1])
        temp = new_ll
        for num in new_num[1::-1]:
            temp.next = ListNode(int(num))
            temp = temp.next
            
        return new_ll