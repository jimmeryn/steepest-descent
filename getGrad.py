import sympy as sp


def getGrad(problem_size, grad, replacements0):
    grad03 = 0
    grad04 = 0
    grad05 = 0

    grad01 = grad[0].subs(replacements0).evalf()
    grad02 = grad[1].subs(replacements0).evalf()
    if problem_size > 2:
        grad03 = grad[2].subs(replacements0).evalf()
    if problem_size > 3:
        grad04 = grad[3].subs(replacements0).evalf()
    if problem_size > 4:
        grad05 = grad[4].subs(replacements0).evalf()

    if problem_size == 2:
        grad0 = sp.Matrix([grad01, grad02])
    if problem_size == 3:
        grad0 = sp.Matrix([grad01, grad02, grad03])
    if problem_size == 4:
        grad0 = sp.Matrix([grad01, grad02, grad03, grad04])
    if problem_size == 5:
        grad0 = sp.Matrix([grad01, grad02, grad03, grad04, grad05])
    return grad0
