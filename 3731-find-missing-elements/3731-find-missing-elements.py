class Solution(object):
    def findMissingElements(self, nums):
        nums=sorted(nums)
        
        result=[]
        for i in range(nums[0],nums[-1]+1):
            if i not in nums:
                result.append(i)
        return result
        
        


        
            

        