class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        primes =[1]*(A+1)
        primes[0]= 0
        primes[1] =0
        for i in range(2,(A+1)):
            if(primes[i]==1):
                for j in range(2*i,A+1, i):
                    primes[j]=0
        p = []
        for k in range(len(primes)):
            if primes[k]==1:
                p.append(k)
            
        s= 0
        
        for i in p:
            if A-i in p:
                s= i
                break
        return [s,A-s]
