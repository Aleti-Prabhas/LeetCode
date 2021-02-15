class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x>=0):
            num=str(x)
            length=len(num)
            count=0
        
            for i in range(0,int(length/2)):
                 if(num[i]==num[length-1-i]):
                     count=count+1
                 else:
                   return "false"
            return "true"
        elif(x<0):
            return "false"
        
