class Solution:
    # @param A : integer
    # @return a strings
    def intToRoman(self, A):
        value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        numericals ={1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}
        res , i = "", 0
        if  A < 1 or A > 3999 :
            return res
        while A :
            res += (A//value[i])*numericals[value[i]]
            A %= value[i]
            i += 1
        return res
