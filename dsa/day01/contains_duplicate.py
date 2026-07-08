class Solution(object):
    def containsDuplicate(self, nums):
        seen ={}
        for i,num in enumerate(nums):
            if num in seen:
                return True
            
            seen[num] = True
        return False
        