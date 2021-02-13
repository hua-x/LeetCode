class Solution:
    
    def isMatch(self, s: str, p: str) -> bool:
        length_s = len(s)
        length_p = len(p)
        df = [[None for j in range(length_p+1)] for i in range(length_s+1)]
        
        df[0][0] =True
        for i in range(1, length_s + 1):
            df[i][0] = False
        for j in range(1, length_p + 1):
            if j % 2 == 0 and p[j-1] == '*':
                df[0][j] = df[0][j-2]
            else:
                df[0][j] = False
        for i in range(1, length_s + 1):
            for j in range(1, length_p + 1):
                if s[i-1] == p[j-1] or p[j-1] == '.': 
                    df[i][j] = df[i-1][j-1]
                elif p[j-1] == '*':
                    if p[j-2] == s[i-1] or p[j-2] == '.':
                        df[i][j] = df[i-1][j] or df[i][j-2] or df[i][j-1]
                    else:
                        df[i][j] = df[i][j-2] #or df[i-1][j] 
                else:
                    df[i][j] = False
        return df



if __name__ == '__main__':
    
    #s = 'aa'
    #p = 'a*'
    #s = 'mississippi'
    #p = 'mis*is*p*.'
    s = 'ab'
    p = '.*'
    solution = Solution()
    
    def output(df, s):
        for i in range(len(s)+1):
            print(s[:i])
            print(df[i])
        #print("final output:")
        #print(solution[len(s)][-1])

    print('=====')

    s1 = 'aa'
    p1 = 'a*'
    df = solution.isMatch(s1,p1)
    output(df,s1)

    print('=====')

    s2 = 'mississippi'
    p2 = 'mis*is*p*.'
    df = solution.isMatch(s2,p2)
    output(df,s2)

    print('=====')

    s3 = 'aa'
    p3 = 'a'
    df = solution.isMatch(s3,p3)
    output(df,s3)

    print('=====')

    s4 = 'aab'
    p4 = 'c*a*b'
    df = solution.isMatch(s4,p4)
    output(df,s4)

    s5 = 'aaa'
    p5 = 'ab*a*c*a'
    df = solution.isMatch(s5,p5)
    output(df,s5)

    
    
    
