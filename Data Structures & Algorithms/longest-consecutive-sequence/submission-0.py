class Solution:
    def longestConsecutive(self, num: List[int]) -> int:
        longest = 0
        nums = set(num)

        for i in nums:
            if i-1 not in nums:
                length =1
            
                while i+length in nums:
                    length += 1

                longest = max(longest, length)

        return longest


    #     num_set = set(nums)
    # longest = 0

    # for num in num_set:
    #     if num - 1 not in num_set:

    #         length = 1

    #         while num + length in num_set:
    #             length += 1

    #         longest = max(longest, length)

    # return longest