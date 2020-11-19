import math

def isPalindrome(x: int) -> bool:

        if x < 0:
            return False, x
        if x < 10:
            return True, x

        tmp = x
        reverse_num = 0
        length = int(math.log10(tmp))+1
        count = length // 2

        for i in range(count):
            reverse_num += tmp % 10 * 10**(count - i -1)
            tmp = tmp//10

        if length % 2 != 0:
            tmp = tmp // 10
            
        return tmp == reverse_num, reverse_num



def isPalindrome_another_approach(x):
        if x < 0:
            return False

        ranger = 1
        while x // ranger >= 10:
            ranger *= 10

        while x:
            left = x // ranger
            right = x % 10
            if left != right:
                return False
            
            x = (x % ranger) // 10
            ranger //= 100

        return True


def print_result(s):
	print(s)
	result, num = isPalindrome(s) 	
	print(result)
	print(num)

if __name__ == '__main__':
	print_result(121)
	print_result(-121)
	print_result(10)
	print_result(-101)
	print_result(0)

