class Solution:
    def mySqrt(self, x: int) -> int:
        sq=None
        if x>=0 and x<=((2**31)-1):
            n=((x//2)+1)
            for i in range (0,n+1):
                if (i*i)==x:
                    sq=i
                    break
                elif (i*i)>x:
                    sq=i-1
                    break
                else:
                    continue
        
        return sq

        