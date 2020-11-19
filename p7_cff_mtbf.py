# Relationships among Reliability Terms
# find CFF and MTBF.
# Valentyn Kuts
#
import math


# function lets enter Reliability and Enter Magnitude of life
def enter_r_t():
    print("Value must be more 0.0 and up to 1.0")
    r = float(input(f"Enter Reliability (R):  "))
    while r <= 0.0 or r > 1.0:
        print("Value must be more 0.0 and up to 1.0")
        r = float(input(f"Enter Reliability (R): "))
    t = float(input(f"Enter Magnitude of life (T): "))
    while t < 0.0:
        print("Value must not be negative")
        t = float(input(f"Enter Magnitude of life (T): "))
    return r, t


# function calculates Cumulative Fault Frequency (CFF)
def calc_cff(r):
    try:
        if r > 0:
            cff = -math.log(r, math.e)
            print("Cumulative Fault Frequency (CFF): ", round(cff, 3))
        else:
            print(" Reliability must be more than 0")
    except ArithmeticError:
        print("Argument must be more 0.0 and up to 1.0")
    return cff


# function calculates Mean Time Between Failure (MTBF)
def calc_mtbf(t, cff):
    try:
        mtbf = t / cff
        print("Mean Time Between Failure (MTBF): ", round(mtbf, 3))
    except ZeroDivisionError:
        print("You cannot divide by zero.")
    except ArithmeticError:
        print("Argument must be more 0.0 and up to 1.0")
    return mtbf


rel, t = enter_r_t()
cff = calc_cff(rel)
mtbf = calc_mtbf(t, cff)
