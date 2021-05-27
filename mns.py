import sympy as sp
from goldstein import goldstein
from getGrad import getGrad
from is_point_minimum import is_point_minimum

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

        if k > 1:
            replacements0 = [("x" + str(i), xk[i - 1]) for i in range(1, problem_size + 1)]
            oldx = xk

        grad0 = getGrad(problem_size, grad, replacements0)

        scalar_product = (grad0.T * grad0)[0]
        if scalar_product <= epsilon:
            logger(
                "Osiągnięto warunek stopu zależny od iloczynu skalarnego gradientów w punkcie "
                + str(xk)
                + " po "
                + str(k-1)
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
                    + " Osiągając kryterium stopu równe: "
                    + str(ispointsclose)
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
                    + " Osiągając kryterium stopu równe: "
                    + str(isvaluessclose)
                )
                condition_type = None
                extreme_type = 3
                if not is_point_minimum(fun, xk):
                    logger("Jednakże znaleziony punkt nie jest minimum. Hesjan nie jest dodatnio określony.")
                    extreme_type = 1
                else:
                    extreme_type = 0
                return {"points": vec_xk, "condition_type": condition_type, "extreme_type": extreme_type}

        replacementsnewk = [("x" + str(i), xk[i - 1]) for i in range(1, problem_size + 1)]
        grad0 = getGrad(problem_size, grad, replacementsnewk)

        scalar_product = (grad0.T * grad0)[0]
        logger(
            "Iteracja "
            + str(k)
            + ". \nPunkt:\n"
            + str(xk[0])
            + "\n"
            + str(xk[1])
            + "\nWartosc:\n"
            + str(fun.subs(replacementsnewk))
            + "\nKryterium stopu:\n"
            + str(scalar_product)
        )

    logger("Nie udało się znaleźć minimum w " + str(k) + " iteracjach.")
    logger(str(xk))
    return {"points": vec_xk, "condition_type": None, "extreme_type": None}
