#You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].
#Input: nums = [5,2,6,1]
#Output: [2,1,1,0]
#Explanation:
#To the right of 5 there are 2 smaller elements (2 and 1).
#To the right of 2 there is only 1 smaller element (1).
#To the right of 6 there is 1 smaller element (1).
#

#naive approach
def countSmaller(arr):
    ans = []
    for i in range(len(arr)):
        count = 0
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                count += 1
        ans.append(count)
    return ans

arr = [5,2,6,1]
countSmaller(arr)
# Time complexity O(n^2)
# Space Complexity O(n)

#O(nlogn)
def countSmaller(arr):
        sorted_arr = []
        rst = []
        for num in arr[::-1]:
            idx = bisect_left(sorted_arr,arr)
            rst.append(idx)
            sorted_arr.insert(idx,num)
        return rst[::-1]

arr = [5,2,6,1]
countSmaller(arr)
