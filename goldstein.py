import sympy as sp
from errorhandlers.goldstein_values_exception import goldstein_values_exception

# Wstępnie rozpisze goldsteina jako pojedyncza funkcje i potem ewentualnie to sie jakos rozbije
# bo jeszcze sam do konca nie jestem pewien jak to powinno dzialac

# start - punkt początkowy
# d - kierunek będący wektorem
# beta - wspolczynnik testu (0, 1/2)
# tauR - początkowa wartość kroku
# epsilon - dokładność
# function - wpisana przez użytkownika funkcja, to trzeba dostosować do parsera


def goldstein(start, d, beta, tauR, epsilon, function):
    problem_size = sp.shape(start)[0]  # ilość zmiennych uzależniam od wymiaru punktu startowego
    goldstein_values_exception(problem_size, tauR, beta)

    grad = []  # gradient na symbolach, lista w praktyce zawierająca między 2, a 5 elementów
    variables = []  # lista zmiennych wstepnie bym przyjął zgodnie z konwencją x1, x2, x3...

    # poniżej test, w tym miejscu trzeba odpowiednio podstawić function pod fun
    fun = sp.parse_expr(function)
    # print(fun)

    # krok 1
    # na listę zmiennych wrzucamy kolejne zmienne zależnie od rozmiaru zadania
    for i in range(1, problem_size + 1):
        variables.append(
            sp.symbols("x" + str(i))
        )  # zgodnie z tą konwencją wsyzstkie zmienne muszą być wprowadzane, jako xn
    for i in range(0, problem_size):
        grad.append(sp.Derivative(fun, variables[i], evaluate=True))  # Tworzę listę z kolejnych pochodnych cząstkowych

    # zasadniczo niepotrzebne, ale pozwoli uniknąć błędów na poziomie testów
    grad03 = 0
    grad04 = 0
    grad05 = 0
    # print(sp.Derivative(sp.log(x1,3),'x1', evaluate=True))
    # wektor zastąpień do metody subs, robi robote
    replacements0 = [("x" + str(i), start[i - 1]) for i in range(1, problem_size + 1)]
    # poniżej dość prymitywnie, ale na potrzeby projektu wystarczająco
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

    p = (
        grad0.T * d
    )[0]  # p jest skalarem, ale w sympy wynik mnożenia macierzy zawsze jest macierzą, więc to przypisanie jest
    # p = p[0]  #  konieczne dla zamierzonego efektu, tu można też dodać obsługę błędu, gdyby p jednak nie było skalarem
    # otrzymane p jest pochodną w kierunku i jej obliczenie, to pierwszy krok w Goldsteinie

    tauL = 0  # tak by wynikało z pokazanego przykładu, nie mam pewności

    replacementstauR = [("x" + str(i), start[i - 1] + tauR * d[i - 1]) for i in range(1, problem_size + 1)]

    # sprawdzenie warunku
    if fun.subs(replacementstauR).evalf() < fun.subs(replacements0).evalf():
        return tauR
        # print("f(x0 + taud) = " + str(fun.subs(replacementstauR).evalf()))
        # print("f(x0) = " + str(fun.subs(replacements0).evalf()))
        # print("Warunek (1) nie zachodzi")

    # poniżej główna pętla algorytmu, bez większej filozofii, zgodnie ze źródłami
    # krok 2
    k = 0
    while k < 1000:

        tau = 1 / 2 * (tauL + tauR)
        if k<1:
            tau = tauR
        replacementstau = [("x" + str(i), start[i - 1] + tau * d[i - 1]) for i in range(1, problem_size + 1)]
        fxtaud = fun.subs(replacementstau).evalf()
        k += 1
        # print(fun.subs(replacements0).evalf() + (1 - beta) * p * tau)
        # print(fun.subs(replacements0).evalf() + beta * p * tau)
        # print(fun.subs(replacements0).evalf())
        # print(fxtaud)
        # krok 3
        if (
            fxtaud < fun.subs(replacements0).evalf() + (1 - beta) * p * tau - epsilon
        ):  # nie jestem pewien cyz sensownie tu te epsilony postawilem
            tauL = tau
            print("weszlo tauL")
        # krok 4
        elif fxtaud > fun.subs(replacements0).evalf() + beta * p * tau + epsilon:
            tauR = tau
            print("weszlo tauR")
        else:
            print("Ilość iteracji Goldstein: " + str(k))
            print("Tau: " + str(tau))  # test
            return tau
    # jeśli w odpowiedniej liczbie iteracji nie dojdziemy do zadanego tau, to zwracamy do czego doszliśmy
    print("Nie udało się znaleźć warotści tau z zadaną dokłandością, po " + str(k) + " iteracjach.")

    print(tau)
    return 0
