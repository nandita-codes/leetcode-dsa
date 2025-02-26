# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
# n=10; g=5; g=g+((n-g)//2)

class Solution:
    def guessNumber(self, n: int) -> int:
        if n==1:
            return n
        l,r = 1,n
        while l<=r:
            mid = l+ (r-l)//2
            g = guess(mid)
            if g==0:
                return mid
            elif g==-1:
                r=mid-1
            elif g==1:
                l=mid+1
        
