'''
Given a string s, find the length of the longest substring without repeating characters.
 '''

# this solution works, but takes too long for the last test on LeetCode
class SolutionOne(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # check string from s[0:len(s)]
        # if there are no repeating characters then record the length of that string
        # if there are repeating characters check all strings of length len(s) - 1
        # if there are repeating characters check all strings of length len(s) - 2
        # ...
        # if there are repeating characters check all strings of length len(s) - [len(s) - 1] = 1 <-- default longest_string_length

        if len(s) == 0:
            return 0    

        for i in range(len(s)):
            # check every word of length len(s) - i
            for j in range(i+1):
                string = s[j:string_length+j]
                #print('string[{},{}] = {}'.format(j, string_length+j, string))


                # check that there are no duplicate letters
                existing_letters = []
                no_duplicates = True
                for l in string:
                    if l not in existing_letters:
                        existing_letters.append(l)
                    else:
                        no_duplicates = False
                        break

                if no_duplicates:
                    return len(string)
                    

class SolutionTwo(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        """ Steps 

        1. Set up the left pointer at 0 and right pointer at 1
        2. Set up an empty dictionary to store letters and their indices
            key --> letter
            val --> index of the letter
        3. Set up the longest string length as 0

        4. Move the right pointer by 1 every round
        5. Check if the new letter is in the dictionary

        IF NOT IN DICTIONARY

        6. set the longest string length to the max of
            - the current longest string length;
            - the right pointer minus the left pointer plus 1 (right - left + 1)

        7. add the current letter and its index to the dictionary

        IF IN DICTIONARY

        6. set the left pointer to the letter to the right of the previous time the current letter was seen

        7. set the longest string length to the max of
            - the current longest string length;
            - the right pointer minus the left pointer plus 1 (right - left + 1)

        8. update the letter's value in the dictionary to the current index


        """

        letters = {}
        left_pointer = 0
        max_string_length = 0

        for right_pointer in range(0, len(s)):
            letter = s[right_pointer]

            if letter not in letters:
                max_string_length = max(max_string_length, right_pointer-left_pointer+1)
            
            else:
                # letter is not in current window
                if letters[letter] < left_pointer:
                    max_string_length = max(max_string_length, right_pointer-left_pointer+1)
                
                # letter is  in current window
                else:
                    left_pointer = letters[letter] + 1
                    
                

            letters[letter] = right_pointer

            print('letter = {}, max_string_length = {}, left_pointer = {}, right_pointer = {}'.format(letter, max_string_length, left_pointer, right_pointer))

        print(letters)
        return max_string_length




if __name__ == '__main__':

    s = 'abac'
    length = SolutionTwo().lengthOfLongestSubstring(s)
    print(length)