class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if  k <= 0:
            return []
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        buckets = [[] for _ in range(len(nums)+1)]
        result = []
        for num, frequency in counts.items():
            buckets[frequency].append(num)
        for i in reversed(range(len(nums)+1)):
            for num in buckets[i]:
                result.append(num)
                k -= 1
            if k == 0:
                return result
