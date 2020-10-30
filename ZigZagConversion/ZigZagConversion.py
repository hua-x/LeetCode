class Solution:
    def convert(self, s: str, numRows: int) -> str:
        s_len = len(s)
        if numRows == 1:
            return s
        
        grp_size = 2 * numRows - 2
        rows = ['' for _ in range(numRows)]
        groups = [s[i:i+grp_size] for i in range(0, s_len, grp_size)]
        for grp in groups:
            for j in range(len(grp)):
                if j < numRows:
                    rows[j] += grp[j]
                else:
                    rows[grp_size-j] += grp[j] 
        
        return ''.join(rows)
