class Solution(object):
    def minSteps(self, s, t):
        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        steps = 0

        for ch in t:
            if ch in count and count[ch] > 0:
                count[ch] -= 1
            else:
                steps += 1

        return steps
