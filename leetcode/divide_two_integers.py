#https://leetcode.com/problems/divide-two-integers/

def divide(self, dividend: int, divisor: int) -> int:
        flagd=0
        flagv=0
        if dividend<0:
            dividend= -dividend
            flagd=1
        if divisor<0:
            divisor=-divisor
            flagv=1
        start=0
        end=dividend
        ans=0
        while start<=end:
            mid=(start+end)//2
            if divisor*mid>dividend:
                end=mid-1
            else:
                ans=mid
                start=mid+1
        return -ans if (flagd^flagv) else min(ans,2147483647)