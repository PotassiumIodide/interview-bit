class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        A= ''.join(filter(str.isalnum,A))
        A=A.lower()
        i=0
        while i<=len(A)-i-1:
            if A[i]!= A[len(A)-i-1]:
                return 0        
            i = i+1
        return 1
