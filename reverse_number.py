class Solution:
    def reverse(self, x: int) -> int:
        a = str(x)

        if 0 < x <= (2**31)-1:
            ans=int(a[::-1])
            if(0<ans<=(2**31)-1):
                return ans
            else:
                return 0

        elif (-2**31) <= x < 0:
            ans=-(int(a[:-len(a):-1]))
            if((-2**31) <= ans < 0):
                return ans
            else:
                return 0
        else:
            return 0
