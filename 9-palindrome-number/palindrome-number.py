class Solution:
    def isPalindrome(self, x: int) -> bool:
        r=0
        n=x
        if x<0:
            return False
        if x<=((2**31)-1):
            while n>0:
                d=n%10
                r=(r*10)+d
                n=n//10
        if x==r:
            return True
        else:
            return False


        