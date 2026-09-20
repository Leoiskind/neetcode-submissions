class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        bucket = [[] for i in range(len(nums) + 1)]
        for i in counts:
            bucket[counts[i]].append(i)

        retList = []
        for i in range(len(bucket)):
            for j in range(len(bucket[-i-1])):
                retList.append(bucket[-i-1][j])
                if len(retList) == k:
                    return retList

        return retList
        