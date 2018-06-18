class Solution:
	# @param A : integer
	# @return a strings
	def countAndSay(self, A):
	    if A==1:
	        return '1'
        if A==2:
            return '11'
        
        string ='11'    
        for  i in range(2,A):
            count =1
            temp = ''
            string+='$' #Dummy Variable to increase length of string
            for j in range(1,len(string)):
                if string[j]==string[j-1]:
                    count +=1
                else:
                    temp= temp +str(count) + string[j-1]
                    count = 1
            string = temp
        return string
	            
	        
	    
