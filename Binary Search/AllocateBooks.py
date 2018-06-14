import itertools
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def ispaintable(self,arr,stud,page):
        students =0
        curpages =arr[0]
        for i in itertools.islice(arr, 1, None):
            if curpages + i >page:
                curpages = i
                students+=1
                if students>=stud :
                    return False
            else:
                curpages+=i
        return True
                
    def books(self, A, B):
        if B>len(A):
            return -1
        maxtime = sum(A)
        
        start = max(A)
        end =maxtime
        while start<=end:
            mid = (start+end)//2
            if self.ispaintable(A,B,mid):
                end =mid-1
            else:
                start = mid+1
        return start

