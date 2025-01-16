from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []

        def backtrack(i:int):
            if i == n:
                res.append(sol[:])
                return
            
            # skip side
            backtrack(i + 1)

            sol.append(nums[i])
            backtrack(i + 1)
            sol.pop()

        backtrack(0)
        return res
    


# Test
s = Solution()
print(s.subsets([1,2,3])) # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

