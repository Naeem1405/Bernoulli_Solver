import sympy as sp
from sympy import *
import latex2mathml.converter

def solve_func(p_str, q_str, n):
    x, y, c = sp.symbols("x y c")
    # y = sp.Function("y")(x)
    euler_dict = {'e': E}
    n = float(n)

    # p_str = input("coeff of p: ")
    # q_str = input("coeff of q: ")
    # n = float(input("n: "))
    p_eq = sympify(p_str, locals=euler_dict)
    q_eq = sympify(q_str, locals=euler_dict)

    i_f = integrate(((1 - n) * p_eq), x)
    i_f = exp(i_f)

    lhs_eq = (y ** (1 - n)) * i_f
    rhs_eq = integrate(((1 - n) * q_eq * i_f), x)
    f = rhs_eq.find(erf)
    for item in f:
        if item == erf(x):
            rhs_eq = Integral(((1 - n) * q_eq * i_f), x)
    rhs_eq = rhs_eq + c
    solv = sp.Eq(lhs_eq, rhs_eq)
    solv = latex(solv)
    solv = latex2mathml.converter.convert(solv)
    return solv


p_str = '1/x'
q_str = '1'
n = '2'
ans = solve_func(p_str, q_str, n)
print(ans)