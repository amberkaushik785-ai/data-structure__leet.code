# OPTIMAL SOLUTION USING HASHMAPS
class solution:
    def TwoSum(self,nums,target):
        seen={}
        for i in range(len(nums)):
            compliment=target-nums[i]

            if compliment in seen :
                return [seen[compliment],i]
            seen[nums[i]]=i

nums=[2,7,11,15]
target=9 

s=solution()
print(s.TwoSum(nums,target))