import math

# Accelerated Experiments for Components
def find_test_duration (x, n, pn, fx, b):

    w_1 = (1/n) * (math.log(1/(1-pn)))
    w_2 = math.log(1/(1-fx))
    w_3 = math.pow(w_1/w_2, 1/b)
    w_4 = w_3*x

    duration = str(round(w_4*0.001, 2))
    duration_hours = duration + "hours"
    print(f"T = {duration_hours}")

print("--  Parameters  --")
print("Enter X:")
x = float(input())
print("Enter n:")
n = float(input())
print("Enter Pn:")
pn = float(input())
print("Enter f(x):")
fx = float(input())
print("Enter b:")
b = float(input())

find_test_duration(x, n, pn, fx, b)
