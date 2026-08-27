class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # for i, i1 in enumerate(numbers):
        #     for j, j1 in enumerate(numbers):
        #         if i != j and i1 + j1 == target:
        #             return [i+1, j+1]

        seen = {}

        for i, num in enumerate(numbers):
            diff = target - num

            if diff in seen:
                return [seen[diff]+1, i+1]

            seen[num] = i