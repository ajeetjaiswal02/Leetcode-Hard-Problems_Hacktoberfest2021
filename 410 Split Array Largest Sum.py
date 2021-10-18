class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        
        def feasible(arr, m, target):
            
            res = 0
            cnt = 0
            
            for i, a in enumerate(arr):
                if res + a > target:
                    cnt += 1
                    res = 0
                res += a
                if i == len(arr) - 1 and res > 0:
                    cnt += 1
              
            return cnt <= m
        
        l, r = max(nums), sum(nums)

        
        while l < r:
            
            mid = l + (r - l) // 2

            if feasible(nums, m, mid):
                r = mid
            else:
                l = mid + 1
        
        return l
