class Solution:
    def isValid(self, s: str) -> bool:
        #def check_again(s):
        #    if s == '':
        #        return True
        #   elif s.find('{}') != -1 or s.find('()') != -1 or s.find('[]')!= -1:
        #       s_new = s.replace('{}','').replace('()','').replace('[]','')
        #       return check_again(s_new)
        #   else:
        #       return False
        #   
        #return check_again(s)

    # test the stack solution from leetcode.
	stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in mapping:
		top_element = stack.pop() if stack else '#'
		if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
	return not stack
