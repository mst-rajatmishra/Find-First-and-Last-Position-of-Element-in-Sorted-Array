class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_first(nums, target):
            left, right = 0, len(nums) - 1
            first_position = -1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
                if nums[mid] == target:
                    first_position = mid
            return first_position
        
        def find_last(nums, target):
            left, right = 0, len(nums) - 1
            last_position = -1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
                if nums[mid] == target:
                    last_position = mid
            return last_position
        
        first = find_first(nums, target)
        last = find_last(nums, target)
        
        return [first, last] if first != -1 else [-1, -1]


sol = Solution()

nums1 = [5, 7, 7, 8, 8, 10]
target1 = 8
print(sol.searchRange(nums1, target1))  

nums2 = [5, 7, 7, 8, 8, 10]
target2 = 6
print(sol.searchRange(nums2, target2)) 

nums3 = []
target3 = 0
print(sol.searchRange(nums3, target3)) 
from typing import List

