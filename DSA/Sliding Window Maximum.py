from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
    
        res = []
        dq = deque()  
        
        for i in range(len(nums)):
            
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            
            dq.append(i)
  
            if dq[0] == i - k:
                dq.popleft()
            
            if i >= k - 1:
                res.append(nums[dq[0]])
                
        return res