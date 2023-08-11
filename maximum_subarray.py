class Solution(object):
    def maxSubArray_1(self, nums):
        """
        This solution looks at every possible subarray and returns the maximum.
        It's super inefficient and there must be a better way. Maybe with pointers?

        :type nums: List[int]
        :rtype: int
        """
        

if __name__ == '__main__':

    
    example_inputs = [[-2,1,-3,4,-1,2,1,-5,4], [1], [5,4,-1,7,8]]
    example_outputs = [6, 1, 23]

    num_problems = len(example_outputs)

    for i in range(num_problems):
        ins = example_inputs[i]
        sol = Solution().maxSubArray(ins)
        expected_output = example_outputs[i]

        print(f'example {i+1} -- {sol == expected_output}. Expected {expected_output} got {sol}')
