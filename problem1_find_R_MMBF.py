# "Relationship among Size,Confidence,Reliability"
# Estimate R and MMBF
# Dmytro Yurchenko

import math

print("Enter Cumulative Fault Frequency:")
cff = float(input())
print("Enter Magnitude of life:")
t = float(input())

def find_r (cff):
    r = math.exp(-cff)
    r = str(round(r*100, 3))
    r_percents = r + "%"
    print(f"R = {r_percents}")

def find_mtbf (cff, t):
    mmbf = t/cff
    print(f"MMBF = {mmbf} Miles/fault during {t} miles")

find_r(cff)
find_mtbf(cff, t)