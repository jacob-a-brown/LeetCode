'''
Probelm 15

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Notice that the order of the output and the order of the triplets does not matter.
'''

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length_nums = len(nums)

        triplets = []

        for i in range(0, length_nums - 2):
            for j in range(i + 1, length_nums - 1):
                for k in range(j + 1, length_nums):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = [nums[i], nums[j], nums[k]]
                        triplet.sort()
                        if triplet not in triplets:
                            triplets.append(triplet)

        return triplets


    def threeSum_2(self, nums):
        triplets = []

        negatives = []
        zeros = []
        positives = []

        for n in nums:
            if n < 0:
                negatives.append(n)
            elif n == 0:
                zeros.append(n)
            else:
                positives.append(n)

        # turn into sets for faster lookup time
        N = set(negatives)
        P = set(positives)

        # case 1: there is at least 1 zero
        if len(zeros) >= 1:
            for n in negatives:
                if -1*n in P:
                    triplet = [n, -1*n, 0]
                    triplet.sort()
                    if triplet not in triplets:
                        triplets.append(triplet)

        # case 2: there are at least 3 zeros
        if len(zeros) >= 3:
            triplet = [0, 0, 0]
            triplets.append(triplet)

        # case 3: two positives sum to a negative
        if len(positives) >= 2:
            for i in range(0, len(positives) - 1):
                for j in range(i + 1, len(positives)):
                    if  -1*(positives[i] + positives[j]) in N:
                            triplet = [-1*(positives[i] + positives[j]), positives[i], positives[j]]
                            triplet.sort()
                            if triplet not in triplets:
                                triplets.append(triplet)

        # case 4: two negatives sum to a positive
        if len(negatives) >= 2:
            for i in range(0, len(negatives) - 1):
                for j in range(i + 1, len(negatives)):
                    if -1*(negatives[i] + negatives[j]) in P:
                        triplet = [-1*(negatives[i] + negatives[j]), negatives[i], negatives[j]]
                        triplet.sort()
                        if triplet not in triplets:
                            triplets.append(triplet)

        return triplets

if __name__ == '__main__':
    ins = [[-1, 0, 1, 2, -1, -4], [0, 1, 1], [0, 0, 0], [1, -1, -1, 0]]
    expected_outs = [[[-1, -1, 2], [-1, 0, 1]], [], [[0, 0, 0]], [[-1, 0, 1]]]

    for i in range(len(ins)):
        sol = Solution().threeSum_2(ins[i])
        out = expected_outs[i]
        print(f'Example {i+1} is {sol==out} --> Expected {out} got {sol}')