# "Relationship among Size,Confidence,Reliability"
# Estimate the number of samples
# Valentyn Kuts

import math


# function lets enter Confidence and Reliability at confidence
def enter_c_rc():
    print("Value must be more 0.0 and up to 1.0")
    c = float(input(f"Enter Confidence (C): "))
    while c <= 0.0 or c > 1.0:
        print("Value must be more 0.0 and up to 1.0")
        c = float(input(f"Enter Confidence (C): "))
    rc = float(input(f"Enter Reliability at confidence (Rc): "))
    while rc <= 0.0 or rc > 1.0:
        print("Value must be more 0.0 and up to 1.0")
        rc = float(input(f"Enter Reliability at confidence (Rc): "))
    return c, rc


# function calculates the Number of samples
def calc_n(c, rc):
    try:
        n = math.log10(1 - c) / math.log10(rc) - 1
        print("Sample size (n): ", math.floor(n))
    except ZeroDivisionError:
        print("You cannot divide by zero.")
    except ArithmeticError:
        print("Argument must be more 0.0 and up to 1.0")
    return n


conf, rel = enter_c_rc()
n = calc_n(conf, rel)
