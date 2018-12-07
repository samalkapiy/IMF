import Rappture
import sys
from math import *
import numpy as np
from scipy.integrate import odeint
from scipy import optimize

def f(y, x, b, formula):
    return eval(formula)

def calc(y,x,a,formula):
    return eval(formula) # y[0] is int f(x) from 0 to 0


def main():

    # Get arguments

    io = Rappture.library(sys.argv[1])

    #xmin = float(io.get('input.number(min).current'))
    #xmax = float(io.get('input.number(max).current'))
    formula1 = io.get('input.string(formula1).current')
    formula2 = io.get('input.string(formula2).current')
    formula3 = io.get('input.string(formula3).current')
    

    #integrating the function
    
    sol1 = odeint(calc, 0, [0.01,0.08], args=(1, formula1))
    ans1 = sol1[1]

    sol2 = odeint(calc, 0, [0.08,0.5], args=(1, formula2))
    ans2 = (0.08)*sol2[1]

    sol3 = odeint(calc, 0, [0.5,100], args=(1,formula3))
    ans3 = (0.08)*(0.5)*sol3[1]

    # Get base string

    N = ans1+ans2+ans3

    str_tot = 'Total number of stars in the mass range'

    #my_str_base = 'int_0.01^0.08 (' + str(formula) + ') dx  ' 

    # Get compute root of \int_0^x f(x') dx' - a

    #root = optimize.brentq(
    #           calc, xmin, xmax, args=(a,formula)
    #       )

    #my_str = '\nResult of ' + my_str_base +  ' in [' + str(0.01) + \
    #        ', ' + str(0.08) + '] is ' + str(sol[1])

    my_str = '\n Result of' + str_tot + 'is'  + str(N)
    

    io.put('output.string(result1).about.label', 'Total stars')
    io.put('output.string(result1).current', my_str)
    #print(my_str)

    # Check

    #check = calc(root, a, formula)

    #my_str2 = '\nCheck: ' + my_str_base + ' = ' + str(check[0])

    #io.put('output.string(result2).about.label', 'check')
    #io.put('output.string(result2).current', my_str2 )
    #print(my_str2 + '\n')

    Rappture.result(io)

if __name__ == "__main__":
    main()

