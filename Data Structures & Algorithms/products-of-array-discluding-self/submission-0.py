class Solution:
    def productExceptSelf(self, num: List[int]) -> List[int]:
        n = len(num)
        res = [1] * n

        prefix = suffix = 1

        for i in range(n):
            res[i] = prefix
            prefix *= num[i]

        for i in range(n-1, -1, -1):
            res[i] *= suffix
            suffix *= num[i]

        return res
