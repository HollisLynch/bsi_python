import math

# Accelerated Experiments for Components
def find_test_duration (x, n, pn, fx, b):

    w_1 = (1/n) * (math.log(1/(1-pn)))
    w_2 = math.log(1/(1-fx))
    w_3 = math.pow(w_1/w_2, 1/b)
    w_4 = w_3*x

    duration = str(math.floor(w_4*0.001))
    duration_hours = duration + " hours"
    print(f"T = {duration_hours}")

print("--  Parameters  --")
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
