import sympy as sp
from errorhandlers.goldstein_values_exception import goldstein_values_exception
from getGrad import getGrad

# start - punkt początkowy
# d - kierunek będący wektorem
# beta - wspolczynnik testu (0, 1/2)
# tauR - początkowa wartość kroku
# epsilon - dokładność
# function - wpisana przez użytkownika funkcja, to trzeba dostosować do parsera


def goldstein(start, d, beta: float, tauR: float, epsilon: float, function: str, logger):
    problem_size = sp.shape(start)[0]  # ilość zmiennych uzależniamy od wymiaru punktu startowego
    goldstein_values_exception(problem_size, tauR, beta)

    grad = []  # gradient na symbolach, lista w praktyce zawierająca między 2, a 5 elementów
    variables = []  # lista zmiennych zgodnie z konwencją x1, x2, x3...
    fun = sp.parse_expr(function)
    # logger(fun)

    # krok 1
    for i in range(1, problem_size + 1):
        variables.append(
            sp.symbols("x" + str(i))
        )  # zgodnie z tą konwencją wsyzstkie zmienne muszą być wprowadzane, jako xn
    for i in range(0, problem_size):
        grad.append(sp.Derivative(fun, variables[i], evaluate=True))  # Tworzę listę z kolejnych pochodnych cząstkowych

    replacements0 = [("x" + str(i), start[i - 1]) for i in range(1, problem_size + 1)]
    grad0 = getGrad(problem_size, grad, replacements0)

    p = (grad0.T * d)[
        0
    ]  # p jest skalarem, ale w sympy wynik mnożenia macierzy zawsze jest macierzą, więc to przypisanie jest
    # p = p[0]  #  konieczne dla zamierzonego efektu, tu można też dodać obsługę błędu, gdyby p jednak nie było skalarem
    # otrzymane p jest pochodną w kierunku i jej obliczenie, to pierwszy krok w Goldsteinie

    tauL = 0

    replacementstauR = [("x" + str(i), (start[i - 1] + tauR * d[i - 1])) for i in range(1, problem_size + 1)]
    fxzero = fun.subs(replacements0).evalf()
    # sprawdzenie warunku

    if fun.subs(replacementstauR).evalf() < fxzero:
        return tauR

    # krok 2
    k = 0
    while k < 10000:

        tau = 1 / 2 * (tauL + tauR)
        if k < 1:
            tau = tauR
        replacementstau = [("x" + str(i), start[i - 1] + tau * d[i - 1]) for i in range(1, problem_size + 1)]
        fxtaud = fun.subs(replacementstau).evalf()
        k += 1

        # krok 3
        if fxtaud < fxzero + (1 - beta) * p * tau - epsilon:
            tauL = tau

        # krok 4
        elif fxtaud > fxzero + beta * p * tau + epsilon:
            tauR = tau

        else:
            return tau
    # jeśli w odpowiedniej liczbie iteracji nie dojdziemy do zadanego tau, to zwracamy do czego doszliśmy
    logger("Nie udało się znaleźć warotści tau z zadaną dokłandością, po " + str(k) + " iteracjach.")

    logger(tau)
    return 0
