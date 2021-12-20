class Solution:
    def twoSum(nums: [int], target: int) -> [int]:
        for x in range(len(nums)):
            current = nums[x] # save x
            nums = nums[:x] + nums[x+1:] # removes x from nums so we don't use it twice
            if target - current in nums:
                return (x, nums.index(target - current)+1) # return indecies, add 1 to target since current was removed, making the list shorter
            else:
                nums.insert(x,current) # put x back in if there is no pair that adds to target


if __name__ == '__main__':
    n = Solution.twoSum([3,2,4],6) #(1,2)