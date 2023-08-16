'''
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The order of the elements may be changed.
Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
The remaining elements of nums are not important as well as the size of nums.
Return k.
'''

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        return_array = []
        for elem in nums:
            if elem != val:
                return_array.append(elem)
        return len(return_array)

if __name__ == '__main__':

    ins = [[3,2,2,3], [0,1,2,2,3,0,4,2]]
    vals = [3, 2]
    expected_outs = [2, 5]
    for i in range(len(ins)):
        sol = Solution().removeElement(ins[i], vals[i])
        print(f'Example {i+1} is {sol == expected_outs[i]} -- expected {expected_outs[i]} got {sol}')