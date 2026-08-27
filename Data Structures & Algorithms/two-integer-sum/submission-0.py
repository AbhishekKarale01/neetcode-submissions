class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,i1 in enumerate(nums):
            for j,j1 in enumerate(nums):
                if i !=j:
                    if i1+j1 == target:
                        return [i,j]
