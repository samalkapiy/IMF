import Rappture
import sys
import math
from math import *
import numpy as np
from scipy.integrate import odeint
from scipy import optimize

def f(y, x, b, formula):
    return eval(formula)

def calc(y,m,a,formula):
    return eval(formula) # y[0] is int f(x) from 0 to 0

def imf(m,m1_min,m1_max,m2_min,m2_max,m3_min,m3_max,formula1,formula2,formula3):
    if m1_min <= m < m1_max:
        return eval(formula1)
    if m2_min <= m < m2_max:
        return eval(formula2) * 0.08
    if m3_min <= m < m3_max:
        return eval(formula3) * 0.5 * 0.08

# two arrays were created

x=[]
y=[]


def main():

    # Get arguments

    io = Rappture.library(sys.argv[1])

    m1_min = float(io.get('input.number(m1_min).current'))
    m1_max = float(io.get('input.number(m1_max).current'))
    m2_min = float(io.get('input.number(m2_min).current'))
    m2_max = float(io.get('input.number(m2_max).current'))
    m3_min = float(io.get('input.number(m3_min).current'))
    m3_max = float(io.get('input.number(m3_max).current'))
    formula1 = io.get('input.string(formula1).current')
    formula2 = io.get('input.string(formula2).current')
    formula3 = io.get('input.string(formula3).current')
    

    #integrating the function
    
    sol1 = odeint(calc, 0, [m1_min,m1_max], args=(1, formula1))
    ans1 = sol1[1]

    sol2 = odeint(calc, 0, [m2_min,m2_max], args=(1, formula2))
    ans2 = (0.08)*sol2[1]

    sol3 = odeint(calc, 0, [m3_min,m3_max], args=(1, formula3))
    ans3 = (0.08)*(0.5)*sol3[1]

    N = ans1+ans2+ans3
    A=1/N

    str_norm = 'Normalization constant'

    my_str = '\n' + str_norm + ' is :'  + str(A)
    
    io.put('output.string(result1).about.label', 'Normalization constant')
    io.put('output.string(result1).current', my_str)

######################################################################
################# plotting the Graph #################################


    io.put('output.curve(result2).about.label','Kroupa IMF plot',append=0)
    io.put('output.curve(result2).yaxis.label','log(dN/dm)')
    io.put('output.curve(result2).xaxis.label', 'log(m)')

    m = np.arange(m1_min, m3_max, 0.01)
    for i in range(len(m)):
        y.append(math.log(imf(m[i],m1_min,m1_max,m2_min,m2_max,m3_min,m3_max,formula1,formula2,formula3)))
        x.append(math.log(m[i]))

        io.put(
             'output.curve(result2).component.xy','%g %g\n' % (x[i],y[i]), append=1
                )

    Rappture.result(io)

if __name__ == "__main__":
    main()


