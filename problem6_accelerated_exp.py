import math

# Daryna Kovyrina
# QITTO3 p.9
# Accelerated Experiments for Components

# p.10, example 2.1
def find_test_duration (x, n, pn, fx, b):
    try:
        w_1 = (1 / n) * (math.log(1 / (1 - pn)))
        w_2 = math.log(1 / (1 - fx))
        w_3 = math.pow(w_1 / w_2, 1 / b)
        w_4 = w_3 * x

        duration = str(math.floor(w_4))
        duration_hours = duration + " hours"
        print(f"T = {duration_hours}")
        return duration
    except ArithmeticError:
        print("ArithmeticError: attempted to divide by zero or number is too large to represent.")
    except ValueError:
        print("ValueError: received an inappropriate value.")


# example 3.1
def find_confidence (x, b, charact_life):

    fx = 1 - math.e(-math.pow(x/charact_life, b))

    fx = str(round(fx, 5))
    fx_perecent = fx + " %"
    print(fx_perecent)
    return fx

def find_characteristic (x, b, n, pn, t):
    try:
        fr_1 = math.pow(1/n*math.log(1/(1-pn)), 1/b)
        fr_2 = fr_1/t
        fr_3 = math.pow(fr_2, b)
        fx = -((1/fr_3)-1)

        den = math.pow(math.log(1/(1-fx)), 1/b)
        slope = x/den

        characteristic = str(math.floor(slope))
        characteristic_hours = characteristic + " hours"
        print(f"fx= {1-fx}")
        print(f"Characteristic life = {characteristic_hours}")
        return slope
    except ArithmeticError:
        print("ArithmeticError: attempted to divide by zero or number is too large to represent.")
    # except ValueError:
    #     print("ValueError: received an inappropriate value.")

print("1 - calculate test duration")
print("2 - characteristic life")
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

    print("Enter number of samples (n):")
    n = float(input())

    print("Enter confidence level (Pn):")
    pn = float(input())

    print("Enter test duration (t):")
    t = float(input())

    charact_life = find_characteristic(x, b, n, pn, t)
    # if (charact_life):
    #     print("Confidence:")
    #     find_confidence(x, b, charact_life)


