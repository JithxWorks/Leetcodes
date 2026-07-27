class Solution(object):
    def containsDuplicate(self, nums):
        a=set(nums)

        if(len(a) != len(nums)):
            return True
        else:
            return False
        
                

        
                
            