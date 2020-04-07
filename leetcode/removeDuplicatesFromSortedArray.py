class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for pos in range(1,len(nums)): #starts at position 1
            if nums[pos] != nums[count]: #checks if number and previous are different
                count = count + 1 #increments count if they're different
                nums[count] = nums[pos] #advances to next new number
        return count + 1

test = Solution()
print(test.removeDuplicates([1,2,6,6,6,8,9,10,10,10,10,12]))