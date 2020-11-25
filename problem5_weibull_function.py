import math
import numpy

# Daryna Kovyrina
# QITTO3 p.18
# Theories of Weibull Distribution

# p.19
def find_weibull (x, slope_weibull, charact_life):
    weibull = 1 - math.exp(-math.pow((x/charact_life), slope_weibull))
    weibull_percents = str(round(weibull*100, 2)) + "%"
    print(f"f(x) = {weibull_percents}")
    return weibull

def find_weibull_ln (fx, slope_weibull, charact_life):

    fr_1 = slope_weibull * (math.log(charact_life))
    fr_2 = math.log(1/(1-fx))
    fr_3 = math.log(fr_2)

    weibull = math.exp((1/slope_weibull) * (fr_3 + fr_1))
    weibull = str(round(weibull, 5))
    weibull_percents = weibull + "%"
    print(f"x = {weibull_percents}")

print("--  Parameters  --")
print("x0 = Expected minimum value of x")
print("b = Slope of Weibull distribution")
print("0 = Characteristic life")
print("x0:")
x = float(input())
print("b:")
slope_weibull = float(input())
print("0:")
charact_life = float(input())

w = find_weibull(x, slope_weibull, charact_life)

find_weibull_ln(w, slope_weibull, charact_life)