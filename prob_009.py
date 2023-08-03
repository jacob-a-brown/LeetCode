'''
Given an integer x, return true if x is a palindrome, and false otherwise.
'''

class Solution(object):
    def isPalindrome_1(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if x < 0:
            return False

        # convert to string
        sx = str(x)

        # numbers to iterate on
        if len(sx) % 2 == 1:
            ni = (len(sx)-1)//2
        else:
            ni = len(sx)//2

        for i in range(ni):
            if sx[i] != sx[-(i+1)]:
                return False

        return True

    def isPalindrome_2(self, x):
        """
        Done without converting x to a string

        :type x: int
        :rtype: bool
        """
        pass
        

if __name__ == "__main__":

    x = 10
    sol = Solution().isPalindrome_1(x)
    print(sol)
