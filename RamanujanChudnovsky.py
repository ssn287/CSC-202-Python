"""
RamanujanChudnovsky approximates Pi with a given degree of accuracy
   @author: Shelby Neal
   Emplid: 6030859
   Email: ssn287@email.vccs.edu
   Purpose: Programming Assignment #1
"""

# import modules 
from decimal import *
import math
import sys
# set recursion limit
sys.setrecursionlimit(100000)
# set precision limit
getcontext().prec = 1000
# recursive factorial method
def fact(n):
    if(n==0):
        return 1
    else:
        return n*fact(n-1)
def sqrt(n, x, y, e):
    if(x - y <= e):
        return x
    else:
        x = (x + y) / 2
        y = n / x
        return sqrt(n, x, y, e)
# recursive Ramanujan summation
def rama(n):
    if(n==0):
        return Decimal((Decimal(fact(4*n))*(Decimal(26390)*Decimal(n)+Decimal(1103)))
                       /((Decimal(fact(n))**Decimal(4))*(Decimal(396)**(Decimal(4)*Decimal(n)))))
    else:
        return Decimal((Decimal(fact(4*n))*(Decimal(26390)*Decimal(n)+Decimal(1103)))
                       /((Decimal(fact(n))**Decimal(4))*(Decimal(396)**(Decimal(4)*Decimal(n))))
                       +Decimal(rama(n-1)))
# recursive Chudnovsky summation
def chud(n):
    if(n==0):
        return Decimal(((Decimal(-1))**Decimal(n))*((Decimal(fact(6*n))*(Decimal(13591409)+Decimal(545140134)*Decimal(n)))
                       /((Decimal(fact(n))**Decimal(3))*(Decimal(fact(3*n)))*(Decimal(640320)**(Decimal(3)*Decimal(n))))))
    else:
        return Decimal(((Decimal(-1))**Decimal(n))*((Decimal(fact(6*n))*(Decimal(13591409)+Decimal(545140134)*Decimal(n)))
                       /((Decimal(fact(n))**Decimal(3))*(Decimal(fact(3*n)))*(Decimal(640320)**(Decimal(3)*Decimal(n)))))
                       +Decimal(chud(n-1)))
# program runs on a loop to approximate Pi
while True:
    # user assigns value for n
    n = int(input("Enter an Integer Number e.g. 13: "))
    # coefficient for Ramanujan's formula
    c = Decimal(Decimal(1)/(Decimal(sqrt(8, 8, 1, 0.000000000000000000000000000001))/Decimal(9801)))
    # coefficient for Chudnovsky's formula
    d = Decimal(Decimal(1)/(Decimal(1)/(Decimal(53360)*Decimal(sqrt(640320, 640320, 1, 0.000000000000000000000000000001)))))
    # coefficients multiplied by summations to approximate Pi
    rama_pi = c / rama(n)
    chud_pi = d / chud(n)
    # prints output
    print("\nUsing Ramanujan's Formula\n\nThe Value of Pi up to ",n," is ",'{0:.1000f}'.format(rama_pi)
           ,"\n\nUsing Chudnovsky's Formula\n\nThe Value of Pi up to ",n," is ",'{0:.1000f}'.format(chud_pi))