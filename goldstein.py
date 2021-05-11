import sympy as sp
from errorhandlers.goldstein_values_exception import goldstein_values_exception

# start - punkt początkowy
# d - kierunek będący wektorem
# beta - wspolczynnik testu (0, 1/2)
# tauR - początkowa wartość kroku
# epsilon - dokładność
# function - wpisana przez użytkownika funkcja, to trzeba dostosować do parsera


def goldstein(start, d, beta: float, tauR: float, epsilon: float, function: str):
    problem_size = sp.shape(start)[0]  # ilość zmiennych uzależniamy od wymiaru punktu startowego
    goldstein_values_exception(problem_size, tauR, beta)

    grad = []  # gradient na symbolach, lista w praktyce zawierająca między 2, a 5 elementów
    variables = []  # lista zmiennych zgodnie z konwencją x1, x2, x3...
    fun = sp.parse_expr(function)
    # print(fun)

    # krok 1
    for i in range(1, problem_size + 1):
        variables.append(sp.symbols("x" + str(i)))  # zgodnie z tą konwencją wsyzstkie zmienne muszą być wprowadzane, jako xn
    for i in range(0, problem_size):
        grad.append(sp.Derivative(fun, variables[i], evaluate=True))  # Tworzę listę z kolejnych pochodnych cząstkowych

    grad03 = 0
    grad04 = 0
    grad05 = 0

    replacements0 = [("x" + str(i), start[i - 1]) for i in range(1, problem_size + 1)]

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

    p = (grad0.T * d)[
        0
    ]  # p jest skalarem, ale w sympy wynik mnożenia macierzy zawsze jest macierzą, więc to przypisanie jest
    # p = p[0]  #  konieczne dla zamierzonego efektu, tu można też dodać obsługę błędu, gdyby p jednak nie było skalarem
    # otrzymane p jest pochodną w kierunku i jej obliczenie, to pierwszy krok w Goldsteinie

    tauL = 0

    replacementstauR = [("x" + str(i), (start[i - 1] + tauR * d[i - 1])) for i in range(1, problem_size + 1)]

    # sprawdzenie warunku

    if fun.subs(replacementstauR).evalf() < fun.subs(replacements0).evalf():
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
        if (
            fxtaud < fun.subs(replacements0).evalf() + (1 - beta) * p * tau - epsilon
        ):
            tauL = tau

        # krok 4
        elif fxtaud > fun.subs(replacements0).evalf() + beta * p * tau + epsilon:
            tauR = tau

        else:
            return tau
    # jeśli w odpowiedniej liczbie iteracji nie dojdziemy do zadanego tau, to zwracamy do czego doszliśmy
    print("Nie udało się znaleźć warotści tau z zadaną dokłandością, po " + str(k) + " iteracjach.")

    print(tau)
    return 0
