import sympy as sp
from goldstein import goldstein


def mns(start, epsilon, L, beta, tau0, function):
    fun = sp.parse_expr(function)
    xk = start
    problem_size = sp.shape(start)[0]
    variables = []
    grad = []

    for i in range(1, problem_size + 1):
        variables.append(
            sp.symbols("x" + str(i))
        )
    replacements0 = [("x" + str(i), start[i - 1]) for i in range(1, problem_size + 1)]
    tau = tau0
    for k in range(1, L+1):

        for i in range(0, problem_size):
            grad.append(sp.Derivative(fun, variables[i], evaluate=True))

        grad03 = 0
        grad04 = 0
        grad05 = 0
        if k > 1:
            replacements0 = [("x" + str(i), xk[i - 1]) for i in range(1, problem_size + 1)]

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

        scalar_product = (grad0.T * grad0)[0]
        if scalar_product <= epsilon:
            print("Udało się znaleźć minimum funkcji w punkcie " + str(xk) + " po " + str(k) + " iteracjach.")
            return xk

        dk = -grad0
        print("kierunek: " + str(dk))
        tau  = goldstein(xk, dk, beta, tau, epsilon, function)
        xk += tau*dk
        k += 1
        print("Iteracja: " + str(k-1) + ", Punkt: " + str(xk))

    print("Nie udało się znaleźć minimum w " + str(k) + " iteracjach.")
    print(xk)
    return 0

