# Reverse an 32 bit signed integer

# (1). iteratively divide by 10
# Runtime: 32ms, Memory: 14mb
def reverse(self, x: int) -> int:
	tmp = -x if x <0 else x
	sign = -1 if x <0 else 1
	digits = []
	while tmp // 10 > 0:
	    digits.append(tmp%10)
	    tmp = tmp//10
	digits.append(tmp)
	    
	num_dig = len(digits)
	num_rev = 0
	for i in range(num_dig):
	    num_rev += digits[i] * 10 ** (num_dig - i -1) 

	final_num = num_rev * sign

	if final_num > -2**31 and final_num < 2**31 - 1 :
	    return final_num
	else:
	    return 0


# (2). through string function
#


