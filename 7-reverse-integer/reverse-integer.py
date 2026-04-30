class Solution:
    def reverse(self, x: int) -> int:
            r=0
            n=None
            if x<0:
                x=abs(x)
                n=1
            while x>0:
                d=x%10
                r=(r*10)+d
                x=x//10
            if n==1:
                r=-abs(r)
            if r<-2**31 or r>((2**31)-1):
                return 0
            else:
                return r    