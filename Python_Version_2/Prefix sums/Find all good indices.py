class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        for i in range(1, n):
            if nums[i - 1] >= nums[i]:
                prefix[i] = prefix[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                suffix[i] = suffix[i + 1] + 1

        result = []
        for i in range(k, n - k):
            if prefix[i - 1] >= k and suffix[i + 1] >= k:
                result.append(i)
        return result