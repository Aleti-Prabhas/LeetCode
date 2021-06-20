class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        l=[]
        sum=0
        for i in range(0,len(nums)):
            sum=sum+nums[i]
            l.append(sum)
        return l   