import math

print("Enter what you want to calculate: or Rc, or C, or n:")
info = input()


def enter(a,b):
   a = input(f"Enter {a}")
   b = input(f"Enter {b}")
   return a,b
   
if(info == "Rc"):
    C = "Confidence (C): "
    n = "Sample size (n): "
    C,n = enter(C,n)
    #print("Confidence (C): ", C)
    #print("Sample size (n): ", n)
    C = float(C)
    n = int(n)
    Rc = math.pow((1 - C),1/n)
    print("Reliability at confidence (Rc): ", round(Rc,2), "%")
    

if(info == "C"):
    Rc = "Reliability at confidence (Rc): "
    n = "Sample size (n): "
    Rc,n = enter(Rc,n)
    #print("Reliability at confidence (Rc): ", Rc)
    #print("Sample size (n): ", n)
    Rc = float(Rc)
    n = int(n)
    #print(Rc**(n+1))
    #print(math.pow(Rc,n+1))
    C = 1 - math.pow(Rc,n+1)
    print("Confidence (C): ", round(C,2), "%")
    
    
if(info == "n"):
    C = "Confidence (C): "
    Rc = "Reliability at confidence (Rc): "
    C,Rc = enter(C,Rc)
    #print("Confidence (C): ", C)
    #print("Reliability at confidence (Rc): ", Rc)
    C = float(C)
    Rc = float(Rc)
    n = math.log10(1 - C)/math.log10(Rc) - 1
    print("Sample size (n): ", math.floor(n))
    
