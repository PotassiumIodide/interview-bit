class Solution:
	# @param A : integer
	# @param B : integer
	# @param C : list of integers
	# @return an integer
	def ispaintable(self,painter,T,board,time):
	    p =0
	    for i in range(painter):
	        total = 0
	        while(p<len(board) and total+board[p]*T<=time):
	            total += board[p]*T
	            p+=1
        return p==len(board)
	def paint(self, A, B, C):
	    maxtime= 1
	    while not self.ispaintable(A,B,C,maxtime):
	        maxtime *= 2
        
        start = maxtime//2
        end =maxtime
        while start<end:
            mid = (start+end)//2
            if self.ispaintable(A,B,C,mid):
                end = mid
            else:
                start = mid+1
        return start%10000003
