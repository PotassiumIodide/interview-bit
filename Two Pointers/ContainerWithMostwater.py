class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArea(self, A):
        maxarea = 0
        l = 0
        r = len(A) - 1
        while l < r :
            base = r - l
            height = min(A[l], A[r])
            area = base * height
            maxarea = max(area, maxarea)
            if A[l] < A[r] :
                l += 1
            else :
                r -= 1
        return maxarea
                
                    
         
