class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        seen_numbers = {}
        for i in range(len(nums)):
            x = target - nums[i]
            if x in seen_numbers.keys():
                result.append(seen_numbers[x])
                result.append(i)
                return result
            else:
                seen_numbers[nums[i]] = i