'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        summation = 0
        sum_not_found = True
        starting_index = 0


        while sum_not_found:
            for i in range(starting_index+1, len(nums)):
                summation = nums[starting_index] + nums[i]
                if summation == target:
                    sum_not_found = False
                    break

            if sum_not_found is False:
                pass
            else:
                starting_index += 1

        if sum_not_found is False:
            return [starting_index, i]

if __name__ == '__main__':
    numbers = [3,3]
    t = 6

    s = Solution()
    r = s.twoSum(numbers, t)
    print(r)
