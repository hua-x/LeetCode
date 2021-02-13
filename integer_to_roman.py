class Solution:
    def intToRoman(self, num: int) -> str:
        
        lst = []
        divisors = [1000,500,100,50,10,5,1]
        start_num = num
        
        for divisor in divisors:
            lst.append(start_num // divisor)
            start_num = start_num % divisor
            
        romans = ['M','D','C','L','X','V','I']
        output = [i*j for i,j in list(zip(romans,lst))]
        
        if output[2] == 'CCCC' and output[1] == 'D':
            output[1], output[2] = '','CM'
        if output[2] == 'CCCC' and output[1] == '':
            output[1], output[2] = '','CD'
        if output[4] == 'XXXX' and output[3] == 'L':
            output[3], output[4] = '','XC'
        if output[4] == 'XXXX' and output[3] == '':
            output[3], output[4] = '','XL'
        if output[6] == 'IIII' and output[5] == 'V':
            output[5], output[6] = '','IX'
        if output[6] == 'IIII' and output[5] == '':
            output[5], output[6] = '','IV'

        return ''.join(output)


if __name__ == '__main__':
    sol = Solution()
    input = [1994,58,9,4,3]
    for i in input:
        print(sol.intToRoman(i))
