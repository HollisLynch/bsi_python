import math

# Theories of Weibull Distribution
print("--  Parameters  --")
print("Enter Expected Minimum:")
x = float(input())
print("Enter Slope of Weibull distribution:")
slope_weibull = float(input())
print("Enter Characteristic life:")
charact_life = float(input())

def find_weibull (x, slope_weibull, charact_life):
    weibull = 1 - math.exp(- math.pow((x/charact_life), slope_weibull))
    weibull = str(round(weibull*100, 5))
    weibull_percents = weibull + "%"
    print(f"F(x) = {weibull_percents}")

find_weibull(x, slope_weibull, charact_life)