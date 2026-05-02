class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #create a dict containing each character and num of uses in s
        if len(s) != len(t):
            return False
            
        s_dict = {}
        for letter in s:
            if letter not in dict.keys(s_dict):
                s_dict[letter] = 1
            else:
                s_dict[letter] += 1
        print(s_dict)
        #search for t characters in s
        for letter in t:
            if letter not in dict.keys(s_dict) or s_dict[letter] == 0:
                return False
            else:
                s_dict[letter] -= 1
        return True