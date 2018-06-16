class Solution:
    # @param A : string
    # @return an integer
    def power(self, A):
        A =int(A)
        temp = A
        Sum =0
        while A!=0:
            Sum += A%2
            A =A//2
        if Sum == 1 and temp!=1:
            return 1
        else:
            return 0
