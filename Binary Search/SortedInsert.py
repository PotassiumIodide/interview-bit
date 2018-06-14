class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        start = 0
        end =len(A)-1
        while(start<=end):
            mid =(start+end)/2
            if A[mid]==B:
                return mid
            if mid + 1 != len(A) and A[mid] < B < A[mid+1] :
                return mid + 1
            elif mid == len(A) - 1  and A[mid] < B :
                return mid + 1
            elif mid != 0 and A[mid - 1] < B < A[mid] :
                return mid
            elif mid == 0 and A[mid] > B :
                return mid
            if B<A[mid]:
                end =mid-1
            elif B>A[mid]:
                start=mid+1
