class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        dic = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        
        def bt(current_strings, remaining_digits):
            if len(remaining_digits) == 0:
                return current_strings
            latest_strings = []
            s = dic[remaining_digits[0]]
            for new_char in s:
                if current_strings:
                    for string in current_strings:
                        latest_strings.append(string + new_char) 
                else:
                    latest_strings.append(new_char)
            
            return bt(latest_strings, remaining_digits[1:])
                
        return bt([], digits)
        
