class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i1=None
        i2=None
        ind=[]
        l=len(nums)
        for i in range(0,l):
            for j in range(i+1,l):
                if nums[i]+nums[j]==target:
                    i1=i
                    i2=j
                    break
        ind.append(i1)
        ind.append(i2)
        return ind

        