class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in nums:
            # want to check if num is the start of a sequence
            if (num - 1) not in numSet: # check if number before exists (0 <- 1)
                length = 0
                while (num + length) in numSet: # check numbers after the first num (1 -> 2 -> 3 -> 4)
                    length += 1
                longest = max(length, longest)
        
        return longest