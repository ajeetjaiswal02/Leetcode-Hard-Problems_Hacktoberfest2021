"""
#239 - https://leetcode.com/problems/sliding-window-maximum/

You are given an array of integers nums, there is a sliding window of size k
which is moving from the very left of the array to the very right.
You can only see the k numbers in the window.
Each time the sliding window moves right by one position.

Return the max sliding window.

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
"""


# Time Complexity - O(n)
# Space Complexity - O(n)


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        res, deque, r = [], [], 0
        while r < len(nums):
            if r >= k and nums[r - k] == deque[0]:
                deque.pop(0)
            while deque and deque[-1] < nums[r]:
                deque.pop()
            deque.append(nums[r])
            if r >= k - 1:
                res.append(deque[0])
            r += 1
        return res


nums = [10, 20, 10, 30, 51, -100, -200, -300, 1000, 29, 290, 2090, 2000]
k = 3
print(Solution().maxSlidingWindow(nums, k))
# [20, 30, 51, 51, 51, -100, 1000, 1000, 1000, 2090, 2090]
