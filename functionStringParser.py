import sympy as sp


def function_string_parser(function_string):
    print(function_string)
    f = sp.parse_expr(function_string)
    print(f.symbols())
    return f
