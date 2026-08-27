class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cou = Counter(nums)

        return [item[0] for item in cou.most_common(k)]