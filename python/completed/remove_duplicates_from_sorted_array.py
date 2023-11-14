'''
Problem 26

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially.
The remaining elements of nums are not important as well as the size of nums.
Return k.
'''

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        seen = set()

        array_length = len(nums)
        array_index = 0

        while array_index < array_length:
            if nums[array_index] not in seen:
                seen.add(nums[array_index])
                array_index += 1
            else:
                nums.pop(array_index)
                array_length -= 1
            
        return len(nums)

    def removeDuplicates2(self, nums):
        left = 0

        for right in range(1, len(nums)):
            if nums[left] != nums[right]:
                nums[left+1] = nums[right]
                left += 1

        return left + 1

if __name__ == '__main__':

    ins = [1,1,2]
    outs = 2

    sol = Solution().removeDuplicates(ins)
    print(f'{sol == outs} -- input is now {ins}')