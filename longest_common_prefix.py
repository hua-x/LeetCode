class Solution:
    def longestCommonPrefix(self, strs):
        lengths = [len(s) for s in strs]
        
        length = min(lengths)
        if (not lengths) or length == 0:
            return ""
        
        string = strs[0]
        i = 1
        longest_prefix = ""
        
        while i <= length:
            common_prefix = string[:i]
            tmp = [s.startswith(common_prefix) for s in strs]
            if all(tmp):
                longest_prefix = common_prefix
            
            i += 1
            
        return longest_prefix
 

if __name__ == '__main__':
    sol = Solution()
    s = ["a"]
    print(sol.longestCommonPrefix(s))
