
## Solution 1 : with hashmap
class Solution(object):
    def twoSum(self,nums,target):
        # Assumption limitation
        if not nums or len(nums)<2:
            return None
        # use HashMap to solve (key,value)
        hashmap = dict()
        # enumerate(): index,value
        for index,value in enumerate(nums):
            if target-value in hashmap:
                # 1st index, 2nd index
                return [index,hashmap[target-vaule]]
            hashmap[value] = index
        return None

## Solution 2: two loops
class Solution(object):
    def twoSum(self,nums,target):
        # Assumption limitation 
        if not nums or len(nums)<2:
            return None
        for index1,value in enumerate(nums):
            for index2 in range(index1+1,len(nums)):
                if nums[index2] == target - value:
                    return [index1,index2]
        return None







