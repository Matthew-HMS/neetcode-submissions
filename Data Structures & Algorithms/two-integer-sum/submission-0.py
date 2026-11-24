class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for i in range(len(nums)):
            dict1[nums[i]] = i

        num = 0
        for i in range(len(nums)):
            num = target - nums[i]
            if num in dict1 and dict1[num] != i:
                return [i, dict1[num]]

        return []