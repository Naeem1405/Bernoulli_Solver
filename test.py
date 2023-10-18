import sympy as sp
from sympy import *



x, y, c = sp.symbols("x y c")
y = sp.Function("y")(x)
euler_dict = {'e': E}

p_str = input("coeff of p: ")
q_str = input("coeff of q: ")
n = float(input("n: "))
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
print(sp.pretty(solv, use_unicode=True))

x_val = int(input("value of x"))
y_val = int(input("value of y"))
eqn = sp.Eq(y.diff(x) + p_eq * y, q_eq * (y**n))
sol = sp.dsolve(eqn, y, ics={y.subs(x, x_val): y_val})
print(sp.pretty(sol, use_unicode=True))

