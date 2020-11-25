import math

# Daryna Kovyrina
# QITTO3 p.9
# Accelerated Experiments for Components
def find_test_duration (x, n, pn, fx, b):

    w_1 = (1/n) * (math.log(1/(1-pn)))
    w_2 = math.log(1/(1-fx))
    w_3 = math.pow(w_1/w_2, 1/b)
    w_4 = w_3*x

    duration = str(math.floor(w_4*0.001))
    duration_hours = duration + " hours"
    print(f"T = {duration_hours}")

def find_confidence (x, b, charact_life):

    fx = 1 - math.e(-math.pow(x/charact_life), b)

    fx = str(round(fx, 5))
    fx_perecent = fx + " %"
    print(f"Confidence = {fx_perecent}")


def find_characteristic (x, b, n, pn, t):

    w_1 = math.pow(1/n*math.log(1/(1-pn)), 1/b)
    print(w_1)
    w_2 = w_1/t
    print(w_2)
    w_3 = math.pow(w_2, b)
    print(w_3)
    fx = -((1/w_3)-1)
    print(1-fx)

    den = math.pow(math.log(1/(1-fx)), 1/b)
    slope = x/den

    characteristic = str(math.floor(slope))
    characteristic_hours = characteristic + " hours"
    print(f"fx= {1-fx}")
    print(f"Characteristic life = {characteristic_hours}")

print("1 - calculate test duration")
print("2 - calculate confidence")
print("3 - characteristic life")
choice = int(input())

if choice == 1:
    print("Enter goal life (x):")
    x = float(input())

    print("Enter number of samples (n):")
    n = float(input())

    print("Enter confidence level (Pn):")
    pn = float(input())

    print("Enter Weibull Slope (b):")
    b = float(input())

    print("Enter reliability level (F(x)):")
    fx = float(input())
    fx = 1 - fx

    find_test_duration(x, n, pn, fx, b)

if choice == 2:
    print("Enter goal life (x):")
    x = float(input())

    print("Enter Weibull Slope (b):")
    b = float(input())

    print("Enter characteristic life (0):")
    charact_life = float(input())

    find_confidence(x, b, charact_life)

if choice == 3:
    print("Enter goal life (x):")
    x = float(input())

    print("Enter Weibull Slope (b):")
    b = float(input())

    print("Enter number of samples (n):")
    n = float(input())

    print("Enter confidence level (Pn):")
    pn = float(input())

    print("Enter test duration (t):")
    t = float(input())

    find_characteristic (x, b, n, pn, t)

