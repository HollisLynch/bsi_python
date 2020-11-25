# "Accelerated experiment for components"
# author: Valentyn Kuts


# To = Test life
# Td = Desired life
# Θ = Characteristic life
# n = Number of samples
# b = Weibull Slope

# find confidence (Pn).

import math


# function lets enter Test life, Characteristic life, Number of samples, Weibull Slope
def enter_to_o_n_b():
    to = float(input(f"Enter Test life (To): "))
    while to < 0.0:
        print("Value must not be negative")
        to = float(input(f"Enter Test life  (To): "))

    o = float(input(f"Enter Characteristic life (Θ): "))
    while o <= 0.0:
        print("Value must be more 0.0 ")
        o = float(input(f"Enter Characteristic life (Θ): "))

    n = float(input(f"Enter Number of samples (n): "))
    while n < 0.0:
        print("Value must not be negative")
        n = float(input(f"Enter Number of samples (n): "))

    b = float(input(f"Enter Weibull Slope (b): "))
    while b < 0.0:
        print("Value must not be negative")
        b = float(input(f"Enter  Weibull Slope (b): "))

    return to, o, n, b


# function calculates confidence (Pn)
def calc_P(to, o, n, b):
    try:
        if o > 0:
            temp = n * math.pow(to / o, b)
            temp = -1*temp
            #print(temp)
            #print(pow(math.e, -temp))
            P = 1 - pow(math.e, temp)
            P = round(P*100, 2)
            print("Confidence (Pn): ", P, " %")
            return P
        else:
            print("  Characteristic life must be more than 0")
    except ZeroDivisionError:
        print("You cannot divide by zero.")
    except ArithmeticError:
        print("Something wrong")


To, O, n, b = enter_to_o_n_b()
P = calc_P(To, O, n, b)
