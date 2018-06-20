class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def threeSum(self, A):
        A.sort()
        result =set()
        for i in range(len(A)-2):
            l = i+1
            r=len(A)-1
            while l<r:
                Sum =A[i]+A[l]+A[r]
                if Sum==0:
                    result.add((A[i],A[l],A[r]))
                    l+=1
                    r-=1
                elif Sum<0:
                    l+=1
                elif Sum>0:
                    r-=1
        arr =list(map(list,result))
        return arr
