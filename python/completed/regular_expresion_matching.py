'''
Problem 10

Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).
'''

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        CHATTY = True

        s_index = 0

        all_letters_all_cases = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

        # used for *s
        skip_next_p_letter_flag = False

        # first case: only 1 letter in s
        if len(s) == 1:
            if p[0] == '.' or p[0] == s[0] and len(p) == 1:
                return True
            else:
                return False

        # second case: only 1 letter in p
        if len(p) == 1 and len(p) != len(s):
            return False

        # third case: p is longer than s and there are no stars
        if len(p) > len(s) and '*' not in p:
            return False

        # fourth case: more than 1 letter in s and more than 1 letter in p
        else:
            for p_index in range(len(p)):
                if skip_next_p_letter_flag:
                    if CHATTY:
                        print('Skipping to the next p letter after wildcard')
                    skip_next_p_letter_flag = False
                    continue

                # matching 0 or more of the preceding element
                if p_index +1 <= len(p) - 1:
                    # automatically matches everything
                    if p[p_index] == '.' and p[p_index+1] == '*':
                        if p[-1] != '*':
                            return False
                        if CHATTY:
                            print('Matching everything')
                        return True

                    if p[p_index] in all_letters_all_cases and p[p_index+1] == '*':
                        skip_next_p_letter_flag = True
                        if s[s_index] != p[p_index]:
                            pass
                            if CHATTY:
                                print(f'Star wildcard for p as \'{p[p_index]}\' != s as \'{s[s_index]}\'')

                        while s[s_index] == p[p_index]:
                            if s_index == len(s) - 1:
                                break
                            if CHATTY:
                                print(f'Found star wildcard. Matching \'{p[p_index]}\' to \'{s[s_index]}\'')
                            s_index += 1

                if skip_next_p_letter_flag is False:
                    # automatically matches any single character.
                    if p[p_index] == '.':
                        if CHATTY:
                            print(f'Found period wildcard. Matching it to {s[s_index]}')
                        # don't advance the s index if we are at the end of p
                        if p_index < len(p) - 1:
                            s_index += 1

                    # match a single letter
                    elif p[p_index] == s[s_index]:
                        if CHATTY:
                            print(f'Matching p as \'{p[p_index]}\' to s as \'{s[s_index]}\'')
                        # don't advance the s index if we are at the end of p
                        if p_index < len(p) - 1:
                            s_index += 1

                    else:
                        if CHATTY:
                            print(f'p as \'{p[p_index]}\' != s as \'{s[s_index]}\' returning False')
                        return False

        # didn't go through all of s after going through all of p
        if s_index < len(s) - 1:
            return False
        else:
            return True


    def isMatch_2(self, s, p):
        '''
        Same as the original isMatch, but it removes the letters from both p and s that have been checked
        '''
        s0 = ' '

        new_s = list(s)
        new_p = list(p)

        CHATTY = True

        all_letters_all_cases = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

        encountered_star = False

        # first case: only 1 letter in s
        if len(new_s) == 1:
            if (new_p[0] == '.' or new_p[0] == new_s[0]) and len(new_p) == 1:
                return True
            elif '*' in new_p:
                pass
            else:
                return False

        # second case: only 1 letter in p
        if len(new_p) == 1 and len(new_p) != len(new_s):
            return False

        # third case: p is longer than s and there are no stars
        if len(new_p) > len(new_s) and '*' not in new_p:
            return False

        # continue to remove letters until either p or s are empty
        while len(new_p) != 0 and len(new_s) != 0:
            if len(new_p) >= 2 and new_p[1] == '*':
                encountered_star = True
                # remove all letters in s
                # remove .* from p
                if new_p[0] == '.' and new_p[1] == '*':
                    s0 = new_s[-1]
                    new_s = []
                    p1 = new_p.pop(1)
                    p0 = new_p.pop(0)

                    if CHATTY:
                        print(f'Removing {p0} and {p1} from p. p is now {new_p}')
                    continue

                if new_p[0] in all_letters_all_cases and new_p[1] == '*':
                    # zero matches, continue
                    if new_s[0] != new_p[0]:
                        p1 = new_p.pop(1)
                        p0 = new_p.pop(0)

                        if CHATTY:
                            print(f'Removing {p0} and {p1} from p. p is now {new_p}')
                        continue

                    # one or more matches
                    while new_s[0] == new_p[0]:
                        s0 = new_s.pop(0)
                        
                        if CHATTY:
                            print(f'Removing {s0} from s. s is now {new_s}')

                        if len(new_s) == 0:
                            break

                    p1 = new_p.pop(1)
                    p0 = new_p.pop(0)

                    # remove any trailing characters who match a previous star wildcard
                    #while len(new_p) > 0 and new_p[0] == s0:
                    #    new_p.pop(0)

                    if CHATTY:
                            print(f'Removing {p0} and {p1} from p. p is now {new_p}')
            else:
                if new_p[0] == '.' or new_p[0] == new_s[0]:

                    s_temp = new_s.pop(0)
                    p_temp = new_p.pop(0)

                    if CHATTY:
                        print(f'Removing {s_temp} from s and {p_temp} from p. s is now {new_s} and p is now {new_p}')

                else:
                    return False

        # can remove any star wildcards from p if there are leftover characters because they can match 0 of them
        # can remove any trailing characters who match the previous star wildcard
        s_index = 0
        nothing_more_to_remove = False
        while len(new_p) > 0:
            if len(new_p) >= 2 and new_p[1] == '*':
                new_p.pop(1)
                new_p.pop(0)
            elif s_index < len(s) and new_p[0] == '.' or new_p[0] == s[s_index]:
                new_p.pop(0)
                s_index += 1                    

            else:
                nothing_more_to_remove = True
            
            if nothing_more_to_remove:
                break

        # if all of the letters have not been removed from s and from p, return False
        if len(new_s) != 0 or len(new_p) != 0:
            return False
        else:
            return True



if __name__ == '__main__':

    in_s = ['aa', 'aa', 'ab', 'mississippi', 'aab', 'aaa', 'ab', 'aab', 'aaa', 'a', 'aaa', 'aaa', 'aaba', 'a', 'bbbba', 'a', 'a', 'a', 'ab']
    in_p = ['a', 'a*', '.*', 'mis*is*p*.', 'c*a*b', 'aa', '.*c', 'c*a*b', 'aaaa', 'ab*a', 'a*a', 'ab*a*c*a', 'ab*a*c*a', 'ab*a', '.*a*a', '.*..a*', '.*..a*', 'ab*', '.*..c*']
    expected_outs = [False, True, True, False, True, False, False, True, False, False, True, True, False, False, True, False, False, True, True]

    for i in range(len(in_s)):
        sol = Solution().isMatch_2(in_s[i], in_p[i])
        print(f'Example {i+1} is {sol==expected_outs[i]} -- expected {expected_outs[i]} got {sol}')
        print('')