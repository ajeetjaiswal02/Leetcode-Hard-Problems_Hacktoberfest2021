"""
#84 - https://leetcode.com/problems/largest-rectangle-in-histogram/

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, 
return the area of the largest rectangle in the histogram.

Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
"""

# Time Complexity : O(n)
# Space Complexity: O(n)

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:    
        heights.append(0)
        ans, stack = 0, [-1]
        for idx, height in enumerate(heights):
            while height < heights[stack[-1]]:
                lastHeight = heights[stack.pop()]
                width = idx - stack[-1] - 1
                ans = max(ans, lastHeight * width)
            stack.append(idx)
        return ans

heights = [10, 29, 123, 23, 29, 19, 10]
print(Solution().largestRectangleArea(heights))
# Output = 123
