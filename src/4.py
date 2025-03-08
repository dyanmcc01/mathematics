import math

def calculate_pi(n):
    # Calculate the value of pi using the Bailey-Borwein-Plouffe formula
    def bbp(n):
        s1 = 0
        t1 = 1
        s2 = 1
        t2 = 0
        for k in range(n):
            k2 = k * 2 + 1
            a = (k2 * k2) - (k * k)
            b = (k2 * k2) - ((k+1) * (k+1))
            c = (k2 * k2) - ((k+1) * (k+1))
            d = k2 * (k2 + 2)
            s3 = a * t1 + b * t2
            t3 = c * s1 + d * s2
            s1 = s2
            s2 = s3
            t1 = t2
            t2 = t3
        return (s1 + s2) / 2 ** n
    # Use the Bailey-Borwein-Plouffe formula to calculate pi with a given number of digits
    digits = int(n)
    pi_digits = []
    for k in range(digits):
        pi_digits.append(str(int(bbp(k+2) * 10 ** 5) % 10))
    return "".join(pi_digits)