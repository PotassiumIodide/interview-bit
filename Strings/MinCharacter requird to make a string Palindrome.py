class Solution:
	# @param A : string
	# @return an integer
	def solve(self, A):
	    if len(A)==0:
	        return 0
        index =1
	    for i in range(1,len(A)):
	        start =0
	        end =i
	        result =True
	        while(start<end):
	            if A[start]!=A[end]:
	                result =False
	                break
	            start+=1
	            end-=1
            if result==True:
                index = i+1
        return len(A)-index
	        
