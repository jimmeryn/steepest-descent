import sympy as sp

# TODO: make visualisation work for any number of args
def function_string_parser(function_string: str):
    print(function_string)
    x1, x2 = sp.symbols("x1,x2")
    f = sp.lambdify([x1, x2], function_string)
    return f
