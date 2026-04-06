class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        s = set(nums)
        longest = 1

        for x in s:
            if x - 1 not in s:
                curr = x
                length = 1

                while curr + 1 in s:
                    curr += 1
                    length += 1

                longest = max(longest, length)

        return longest