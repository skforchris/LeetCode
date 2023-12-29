class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
            return False
        
        x = str(x)
        reverse = x[::-1]

        x = int(x)
        reverse = int(reverse)

       
        if(x - reverse ==0):
            return True
        else:
            return False