import math

def calculate_pi(n):
    """Use the Bailey-Borwein-Plouffe formula to calculate pi to n decimal places"""
    k = 0
    s = 0
    while k < n:
        s += (1/(2*k + 1)) - (1/(2*k + 2))
        k += 1
    return round(s, n)