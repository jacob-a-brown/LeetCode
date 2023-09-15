'''
Problem 28

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

'''

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        num_needle_char = len(needle)
        num_hay_char = len(haystack)

        for i in range(0, num_hay_char - num_needle_char + 1):
            check_str = haystack[i:i+num_needle_char]
            if check_str == needle:
                return i

        return -1

if __name__ == '__main__':
    needles = ['sad', 'leeto', 'a', 'c']
    haystacks = ['sadbutsad', 'leetcode', 'a', 'abc']
    outs = [0, -1, 0, 2]

    for i in range(len(outs)):
        sol = Solution().strStr(haystacks[i], needles[i])
        out = outs[i]
        print(f'Example {i+1} is {sol==out} --> expected {out} got {sol}')