class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict1 = {}
        for n in nums:
            dict1[n] = dict1.get(n, 0) + 1
            if dict1[n] > 1:
                return True

        return False
