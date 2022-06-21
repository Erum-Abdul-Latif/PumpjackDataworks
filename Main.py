import math
####### formula 2
def slope_formula(a,b):
    c=math.pow(a+b,2)
    return c
########

def fourierseries():
    return "monday"
def slopeformula1():
    return "tuesday"
def slopeformula2():
    n1=input('Enter First Number : ')
    n2=input('Enter Second Number : ')
    n1 = float(n1)
    n2 = float(n2)
    print(slope_formula(n1,n2))


def quadraticformula():
    return "thursday"
def laplaceformula():
    return "friday"
def default():
    return "Invalid choice"

switcher = {
    1: fourierseries,
    2: slopeformula1,
    3: slopeformula2,
    4: quadraticformula,
    5: laplaceformula
    }
  
def switch(formula):
    return switcher.get(formula, default)()

if __name__ == "__main__":
    formula = float(input('Enter choice: '))
    print(switch(formula))