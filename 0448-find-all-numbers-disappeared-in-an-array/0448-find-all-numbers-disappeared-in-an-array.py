class Solution(object):
    def findDisappearedNumbers(self, nums):
       a=set(nums)
       b=[]

       for i in range(1, len(nums)+1):
        if(i not in a):
            b.append(i)
       return b

       
    

    

        