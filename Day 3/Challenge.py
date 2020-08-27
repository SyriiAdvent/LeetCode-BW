"""
287. Find the Duplicate Number
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        cache = {}
        for n in nums:
            if n not in cache:
                cache[n] = 1
            else:
                return n