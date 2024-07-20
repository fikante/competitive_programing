class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 0:
            return None 

        if x == 0:
            return 0

        guess = x
        while True:
            next_guess = 0.5 * (guess + x / guess)
            if abs(next_guess - guess) < 1e-7:
                return int(next_guess)
            guess = next_guess

        