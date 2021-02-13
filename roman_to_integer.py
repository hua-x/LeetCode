class Solution:
    def romanToInt(self, s: str) -> int:
        
        import time

        dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        t0 = time.time()
        numbers = [dict[i] for i in s]
        t1 = time.time()
        print(f"map to values takes {t1-t0} secs")
        #ind = [x-y for x,y in zip(numbers[:-1],numbers[1:])]
        ind = [-1 if numbers[i+1] - numbers[i] < 0 else 1 for i in range(len(s)-1)] +[1]
        t2 = time.time()
        print(f"check increment/decrement takes {t2-t1} secs")
        #ind = [-1 if i < 0 else 1 for i in ind] + [1]
        t3 = time.time()
        print(f"convert change to digital takes {t3-t2} secs")
        summation = [i*j for i,j in zip(numbers, ind)]
        t4 = time.time()
        print(f"zip takes {t4-t3} secs")
        return sum(summation)


if __name__ == '__main__':
    sol = Solution()
    #strings = ['IV','III','IX','MCMXCIV']
    strings = ['MCMXCIV']
    for s in strings:
        print(sol.romanToInt(s))
    
