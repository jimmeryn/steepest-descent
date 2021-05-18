import sympy as sp
from goldstein import goldstein

# funckja zwraca listę objektów typu sp.Matrix, są to kolejne punkty osiągane przez algorytm,
# przedostatni punkt to znalezione minimum, natomiast ostatni punkt jest flagą zawierającą informację o typie wyniku,
# pierwsza wartość ostatniego punktu oznacza jakiego typu warunek został spełniony:
# 1 - warunek iloczynu skalarnego gradientów
# 2 - warunek odległości kolejnych punktów
# 3 - warunek różnicy kolejnych wartości
# druga składowa natomiast odpowiada za typ ekstremum
# 0 - minimum
# 1 - nie wiadomo, ale na pewno nie minimum
def mns(start, epsilon: float, L: int, beta: float, tau0: float, function: str, logger):
    fun = sp.parse_expr(function)
    xk = start
    problem_size = sp.shape(start)[0]
    variables = []
    grad = []

    for i in range(1, problem_size + 1):
        variables.append(sp.symbols("x" + str(i)))
    replacements0 = [("x" + str(i), start[i - 1]) for i in range(1, problem_size + 1)]
    tau = tau0
    vec_xk = []
    vec_xk.append(start)
    for k in range(1, L + 1):

        for i in range(0, problem_size):
            grad.append(sp.Derivative(fun, variables[i], evaluate=True))

        grad03 = 0
        grad04 = 0
        grad05 = 0
        if k > 1:
            replacements0 = [("x" + str(i), xk[i - 1]) for i in range(1, problem_size + 1)]
            oldx = xk

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
            logger(
                "Osiągnięto warunek stopu zależny od iloczynu skalarnego gradientów w punkcie "
                + str(xk)
                + " po "
                + str(k)
                + " iteracjach."
            )
            extreme_type = None
            if not is_point_minimum(fun, xk):
                logger("Jednakże znaleziony punkt nie jest minimum. Hesjan nie jest dodatnio określony.")
                extreme_type = 1
            else:
                extreme_type = 0
            return {"points": vec_xk, "condition_type": 1, "extreme_type": extreme_type}

        dk = -grad0
        # logger("kierunek: " + str(dk))
        tau = goldstein(xk, dk, beta, tau0, epsilon, function, logger)
        xk += tau * dk
        vec_xk.append(xk)

        if k > 1:
            ispointsclose = 0
            for i in range(0, problem_size):
                ispointsclose += (xk[i] - oldx[i]) ** 2
            ispointsclose = sp.sqrt(ispointsclose)
            if ispointsclose < epsilon:
                logger(
                    "Osiągnięto warunek stopu zależny od odległości kolejnych punktów "
                    + str(xk)
                    + " i "
                    + str(oldx)
                    + " po "
                    + str(k)
                    + " iteracjach."
                )
                condition_type = None
                extreme_type = None
                if not is_point_minimum(fun, xk):
                    logger("Jednakże znaleziony punkt nie jest minimum. Hesjan nie jest dodatnio określony.")
                    condition_type = 2
                    extreme_type = 1
                else:
                    condition_type = 2
                    extreme_type = 0
                return {"points": vec_xk, "condition_type": condition_type, "extreme_type": extreme_type}

            replacementsnewk = [("x" + str(i), xk[i - 1]) for i in range(1, problem_size + 1)]
            isvaluessclose = abs(fun.subs(replacementsnewk) - fun.subs(replacements0))
            if isvaluessclose < epsilon:
                logger(
                    "Osiągnięto warunek stopu zależny od różnicy kolejnych wartości w punkcie: "
                    + str(xk)
                    + " po "
                    + str(k)
                    + " iteracjach, osiągając wartość: "
                    + str(fun.subs(replacementsnewk))
                )
                condition_type = None
                extreme_type = 3
                if not is_point_minimum(fun, xk):
                    logger("Jednakże znaleziony punkt nie jest minimum. Hesjan nie jest dodatnio określony.")
                    extreme_type = 1
                else:
                    extreme_type = 0
                return {"points": vec_xk, "condition_type": condition_type, "extreme_type": extreme_type}

    logger("Nie udało się znaleźć minimum w " + str(k) + " iteracjach.")
    logger(str(xk))
    return {"points": vec_xk, "condition_type": None, "extreme_type": None}


# zwraca true jesli punkt jest minimum funkcji, false jeśli nie ma do tego pewnosci
def is_point_minimum(function, point):
    problem_size = point.shape[0]
    variables = []

    for i in range(1, problem_size + 1):
        variables.append(sp.symbols("x" + str(i)))

    replacements = [("x" + str(i), point[i - 1]) for i in range(1, problem_size + 1)]
    hess = []

    for i in range(0, problem_size):
        for j in range(0, problem_size):
            hess.append(
                sp.Derivative(sp.Derivative(function, variables[i], evaluate=True), variables[j], evaluate=True)
            )

    # stworzenie długiej listy, by następnie budować z niej macierze jest karkołomne, ale inaczej nie potrafie
    hesjan2 = sp.Matrix([[hess[0], hess[1]], [hess[2 + problem_size - 2], hess[3 + problem_size - 2]]])
    if problem_size > 2:
        hesjan3 = sp.Matrix(
            [
                [hess[0], hess[1], hess[2]],
                [hess[3 + problem_size - 3], hess[4 + problem_size - 3], hess[5 + problem_size - 3]],
                [hess[6 + problem_size - 3], hess[7 + problem_size - 3], hess[8 + problem_size - 3]],
            ]
        )
    if problem_size > 3:
        hesjan4 = sp.Matrix(
            [
                [hess[0], hess[1], hess[2], hess[3]],
                [
                    hess[4 + problem_size - 4],
                    hess[5 + problem_size - 4],
                    hess[6 + problem_size - 4],
                    hess[7 + problem_size - 4],
                ],
                [
                    hess[8 + problem_size - 4],
                    hess[9 + problem_size - 4],
                    hess[10 + problem_size - 4],
                    hess[11 + problem_size - 4],
                ],
                [
                    hess[12 + problem_size - 4],
                    hess[13 + problem_size - 4],
                    hess[14 + problem_size - 4],
                    hess[15 + problem_size - 4],
                ],
            ]
        )
    if problem_size > 4:
        hesjan5 = sp.Matrix(
            [
                [hess[0], hess[1], hess[2], hess[3], hess[4]],
                [hess[5], hess[6], hess[7], hess[8], hess[9]],
                [hess[10], hess[11], hess[12], hess[13], hess[14]],
                [hess[15], hess[16], hess[17], hess[18], hess[19]],
                [hess[20], hess[21], hess[22], hess[23], hess[24]],
            ]
        )

    # sprawdzam wszystkie podwyznaczniki hesjanu, jesli sa dodatnie, to punkt jest minimum
    if hess[0].subs(replacements) <= 0:
        return False
    if hesjan2.subs(replacements).det() <= 0:
        return False
    if problem_size > 2 and hesjan3.subs(replacements).det() <= 0:
        return False
    if problem_size > 3 and hesjan4.subs(replacements).det() <= 0:
        return False
    if problem_size > 4 and hesjan5.subs(replacements).det() <= 0:
        return False

    return True
