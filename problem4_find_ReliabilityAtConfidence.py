# "Relationship among Size,Confidence,Reliability"
# Estimate the find reliability at confidance
# Dmytro Yurchenko
import math

print("Enter Confidance Level:")
c = float(input())
while (c < 0.0 or c > 1.0):
    print("C value must be from 0.0 to 1.0")
    c = float(input())

print("Enter Sample size:")
n = float(input())

def find_rc (c, n):
    rc = math.pow((1 - c), 1/(n + 1))
    rc = str(round(rc*100, 3))
    print(f"Reliability at confudance is: {rc}%.")

find_rc (c, n)
