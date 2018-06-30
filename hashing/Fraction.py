class Solution:
    # @param A : integer
    # @param B : integer
    # @return a strings
    def fractionToDecimal(self, A, B):
        numerator =A
        denominator =B
        sign = 1
        if numerator * denominator < 0: 
            sign = -1
            numerator, denominator = abs(numerator), abs(denominator)
        seenRem = {}
        initVal, remainder = divmod (numerator, denominator)
        res = [str(initVal)]
        count = 1
        while remainder != 0:
            #print (seenRem, res)
            seenRem[remainder] = count
            next, remainder = divmod (remainder * 10, denominator)
            res.append (str(next))
            if remainder in seenRem:
                res.insert (seenRem[remainder], "(")
                res.append (")")
                break
            count += 1
        
        if len(res) > 1:
            res.insert(1, ".")
            
        if sign == 1:
            return "".join(res)
        else:
            return "-"+"".join(res)
