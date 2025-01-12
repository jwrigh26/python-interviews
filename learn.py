from typing import List

# Learning playground
# Today We learning Recursive Backtracking - DSA

# Time O(2^n)
# Space depth of recusion  O(n)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sol = [], [] # result and solution

        def backtrack(i):
            if i == n:
                res.append(sol[:]) # copy a snapshot in time of what sol is storing.
                return
            
            # Don't pick nums[i]
            backtrack(i+1)

            # Pick nums[i]
            sol.append(nums[i])
            backtrack(i + 1)
            sol.pop() # recursively backtrack

        backtrack(0)
        return res
    

# Test
s = Solution()
print(s.subsets([1,2,3])) # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]