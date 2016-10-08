from fractions import Fraction

def minFortnight(minVal):
    fract = minVal * 0.0000496032
    return str(Fraction(fract).limit_denominator())

def hourFortnight(hourVal):
    fract = hourVal * 0.00297619
    return str(Fraction(fract).limit_denominator())

def dayFortnight(dayVal):
    fract = dayVal * 0.0714286
    return str(Fraction(fract).limit_denominator())

print(dayFortnight(4))
