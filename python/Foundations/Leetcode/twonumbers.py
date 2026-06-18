class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #print(f"{len(nums)} intial legnth")
        global i
        global j    
        i =1
        iteration = 0
        output = []
        print("target", target)
        for i in range(0, len(nums)):
            it = nums[i]
            for j in range(i+1, len(nums)):
                se = nums[j]
                total = nums[i]+nums[j]
                if(nums[i]+nums[j]==target and i !=j):
                    print("total", total)
                    output.append(nums.index(nums[i]))
                    output.append(nums.index(nums[j]))
                    print("nums i and j", nums[j], nums[i])
                    return i, j
                    break
                else:
                    print(f"{i}, {j}, {total}-> total")
                    
    print(twoSum(self=0, nums=[1,2,7,4,5], target=5))

#   the goal was to find two numbers in a list that added up to an x number which is known as target
#   this method uses brute forcing to find those two numbers
#
#