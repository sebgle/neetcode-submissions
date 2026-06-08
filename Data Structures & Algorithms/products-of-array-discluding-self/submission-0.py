class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:     
        prefix = [1]
        for i in range(1, len(nums)):
            prefix.append(prefix[i-1] * nums[i-1])
        postfix = [1] * len(nums)
        for i in reversed(range(len(nums) - 1)):
            postfix[i] = postfix[i + 1] * nums[i+1]

        result = []
        for i in range(len(nums)):
            result.append(prefix[i] * postfix[i])

        return result