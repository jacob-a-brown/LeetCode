class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """


        def bisection_search(nums, target, bias):
            left = 0
            right = len(nums) - 1
            index = -1
            while left <= right:
                middle = (left + right) // 2
                if target > nums[middle]:
                    # target is above the middle, so set the left index to the
                    # right of middle (no need to check middle again)
                    left = middle + 1
                elif target < nums[middle]:
                    # target is below the middle, so set the right index to the
                    # left of middle (no need to check middle again)
                    right = middle - 1
                else:
                    # hit the target, so set the index to middle
                    index = middle

                    # continue to search to the sides of the bisection search
                    # to get the leftmost and rightmost indices for the target
                    if bias == 'left':
                        right = middle - 1
                    else:
                        left = middle + 1

            return index

        left_index = bisection_search(nums, target, 'left')
        right_index = bisection_search(nums, target, 'right')

        return [left_index, right_index]

if __name__ == '__main__':

    n = [1, 1, 1, 2, 3, 3, 4, 5, 6]
    t = 8
    print(Solution().searchRange(n, t))