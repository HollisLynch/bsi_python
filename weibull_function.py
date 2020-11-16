import math
import numpy

# Theories of Weibull Distribution
def find_weibull (x, slope_weibull, charact_life):
    weibull = 1 - math.exp(-math.pow((x/charact_life), slope_weibull))
    weibull_percents = str(round(weibull*100, 5)) + "%"
    print(f"f(x) = {weibull_percents}")
    return weibull

def find_weibull_ln (fx, slope_weibull, charact_life):

    w_1 = slope_weibull * (math.log(charact_life))
    w_2 = math.log(1/(1-fx))
    w_3 = math.log(w_2)

    weibull = math.exp((1/slope_weibull) * (w_3 + w_1))
    weibull = str(round(weibull, 5))
    weibull_percents = weibull + "%"
    print(f"x = {weibull_percents}")

print("--  Parameters  --")
print("Enter Expected Minimum:")
x = float(input())
print("Enter Slope of Weibull distribution:")
slope_weibull = float(input())
print("Enter Characteristic life:")
charact_life = float(input())

w = find_weibull(x, slope_weibull, charact_life)

find_weibull_ln(w, slope_weibull, charact_life)