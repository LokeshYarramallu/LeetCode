class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_map = {0: 1}
        sums = 0
        count = 0
        for n in nums:
            sums +=n
            if (sums - k) in sum_map:
                count += sum_map[sums - k]
            sum_map[sums] = sum_map.get(sums, 0) + 1
        return count
