class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            fast = nums[nums[fast]]
            slow = nums[slow]

        slow2 = 0
        while True:
            fast = nums[fast]
            slow2 = nums[slow2]

            if fast == slow2:
                return slow2

        