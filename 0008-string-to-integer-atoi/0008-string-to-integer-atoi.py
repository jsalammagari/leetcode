class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        result = 0
        isNegative=False
        INT_MAX = 2**31 -1
        INT_MIN = -2**31
        while i<len(s) and s[i]==' ':
            i=i+1
        if i<len(s) and s[i]=='+':
            i=i+1
        elif i<len(s) and s[i]=="-":
            i=i+1
            isNegative=True
        while i<len(s) and s[i].isdigit():
            digit=int(s[i])
            if result>(INT_MAX-digit)//10:
                return INT_MIN if isNegative else INT_MAX
            result = result*10+digit
            i = i+1
        return -result if isNegative else result
        