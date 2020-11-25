# "Relationship among Size,Confidence,Reliability"
# Estimate the confidance level
# Dmytro Yurchenko

import math

print("Enter Reliability at confidence:")
rc = float(input())
while (rc < 0.0 or rc > 1.0):
    print("Rc value must be from 0.0 to 1.0")
    rc = float(input())

print("Enter Sample size:")
n = float(input())

def find_c (rc, n):
    c = 1 - math.pow(rc, n + 1)
    c = str(round(c*100, 3))
    print(f"Confidence level is: {c}%.")

find_c (rc, n)
