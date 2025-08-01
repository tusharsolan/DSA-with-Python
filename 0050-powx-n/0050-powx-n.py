class Solution:
    def myPow(self, x: float, n: int) -> float:
        def fast_pow(x, n):
            if n == 0:
                return 1.0
            half = fast_pow(x, n // 2)
            if n % 2 == 0:
                return half * half
            else:
                return half * half * x
        
        if n < 0:
            x = 1 / x
            n = -n
        return fast_pow(x, n)
