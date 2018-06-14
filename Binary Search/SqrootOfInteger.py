class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        mid =0
        start =1
        end =A
        if A==0 or A==1:
            return A
        while (start<=end):
            mid = (start +end)//2
            if mid*mid == A:
                return mid
            elif mid*mid>A:
                end = mid -1
            elif mid*mid <A:
                start = mid+1
                ans =mid
        return ans
