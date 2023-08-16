'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        scene = []


        for elem in nums:
            if elem not in scene:
                scene.append(elem)
            else:
                return True
        return False

if __name__ == '__main__':

    ins = [[1,2,3,4], [1,2,3,4,1], [1,2,3,4,4], [1,2,3,4,2,5,1,8], [1000, 81, 9999, 432, 0]]
    expected = [False, True, True, True, False]
    for i in range(len(ins)):
        sol = Solution().containsDuplicate(ins[i])
        print(f'Example {i+1} is {sol==expected[i]} -- Expected {expected[i]} got {sol}')