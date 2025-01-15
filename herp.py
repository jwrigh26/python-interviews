from typing import List

class Solution:
    def search(self, nums:List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2

            if nums[l] < nums[r]:
                return nums[l]

            if nums[r] < nums[m]:
                l = m + 1 
            else:
                r = m
        return nums[l]

sol = Solution()
print(sol.search([16,17,18,1,2,3]))
