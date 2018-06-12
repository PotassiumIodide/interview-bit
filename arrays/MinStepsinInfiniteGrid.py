class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        #The shortest path is along the diagonal
        #till one of the ordinate is same and then
        #horizontal or vertical
        #So max of (X1-X2) and (Y1-Y2) will be the min
        #steps taken to reach X2,Y2 from X1,Y1 
        steps =0
        for i in range(len(A)-1):
            maxdist =max(abs(A[i]-A[i+1]),abs(B[i]-B[i+1]))
            steps = steps +maxdist
        return steps
