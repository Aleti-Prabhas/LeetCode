class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        finallist=[]
        finallist.append(nums1)
        finallist.append(nums2)
        finallist.sort()
        length=len(finallist)
        if(length%2==0):
            leng=int(length/2)
            x=finallist[leng-1]
            y=finallist[leng]
            sumi=x+y
            ans=sumi/2
            return "{0:.5f}".format(ans)
            
        else:
            leng=int((length+1)/2)
            z=finallist[leng]
            return  "{0:.5f}".format(z)
