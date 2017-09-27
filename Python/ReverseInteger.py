
##  123 -------------------------------> 321
##  (100*1 + 10*2 + 3*1 )          (100*3 + 10*2 + 1*1)
##  get remainder
##  123/10 = 3                        3
##  12/10 =2                          3*10 + 2
##  1/10 =1                           3*10*10 + 2*10 + 1
##    31             31
##  -2    ------>   2     (overflow)


class Solution:
    # @param {int} n the integer to be reversed
    # @return {int} the reversed integer
    def reverseInteger(self, n):
        if n == 0:
            return 0
            
        neg = 1
        if n < 0:
            neg, n = -1, -n
        
        reverse = 0
        while n > 0:
            reverse = reverse * 10 + n % 10
            n = n / 10
        
        reverse = reverse * neg
        if reverse < -(1 << 31) or reverse > (1 << 31) - 1:
            return 0
        return reverse


