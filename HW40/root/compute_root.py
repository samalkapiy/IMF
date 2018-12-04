import Rappture
import sys
from math import *
import numpy as np
from scipy.integrate import odeint
from scipy import optimize

def f(y, x, b, formula):
    return eval(formula)

def calc(x, a, formula):
    y = odeint(f, -a, [0,x], args=(1, formula))
    return y[1]  # y[0] is int f(x) from 0 to 0

def main():

    # Get arguments

    io = Rappture.library(sys.argv[1])

    xmin = float(io.get('input.number(min).current'))
    xmax = float(io.get('input.number(max).current'))
    formula = io.get('input.string(formula).current')
    a = float(io.get('input.number(a).current'))

    #parser = argparse.ArgumentParser(description='Find root')

    #parser.add_argument('formula', type=str, help='f(x)')

    #integrating the function



    # Get base string

    my_str_base = 'int_0^root (' + str(formula) + ') dx - ' + str(a)

    # Get compute root of \int_0^x f(x') dx' - a

    root = optimize.brentq(
               calc, xmin, xmax, args=(a,formula)
           )

    my_str = '\nRoot of ' + my_str_base +  ' in [' + str(xmin) + \
            ', ' + str(xmax) + '] is ' + str(root)

    io.put('output.string(result1).about.label', 'Root')
    io.put('output.string(result1).current', my_str)
    #print(my_str)

    # Check

    check = calc(root, a, formula)

    my_str2 = '\nCheck: ' + my_str_base + ' = ' + str(check[0])

    io.put('output.string(result2).about.label', 'check')
    io.put('output.string(result2).current', my_str2 )
    #print(my_str2 + '\n')

    Rappture.result(io)

if __name__ == "__main__":
    main()

