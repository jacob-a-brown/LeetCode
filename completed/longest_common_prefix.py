'''
Problem 14

Write a function to find the longest common prefix string amonst an array of strings.

If there is no common prefix, return the empty string ""
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        chars = [c for c in strs[0]]
        index = 0
        matched = True

        while index < len(chars) and matched:
            current_char = chars[index]
            # check the character against all other strings
            for string in strs:
                if index > len(string) - 1:
                    matched = False
                    break
                if string[index] != current_char:
                    matched = False
                    break
            if matched:
                index += 1

        matching_chars = strs[0][0:index]
        return matching_chars
        

if __name__ == '__main__':
    ins = [['flower', 'flow', 'flight'], ['dog', 'racecar', 'car'], ['a'], ['ab', 'a']]
    expected_outs = ['fl', '', 'a', 'a']

    for i in range(len(ins)):
        sol = Solution().longestCommonPrefix(ins[i])
        out = expected_outs[i]
        print(f'Example {i+1} is {sol==out} --> expected {out} got {sol}')