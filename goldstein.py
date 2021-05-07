import sympy as sp
from numpy import array

# Wstępnie rozpisze goldsteina jako pojedyncza funkcje i potem ewentualnie to sie jakos rozbije
# bo jeszcze sam do konca nie jestem pewien jak to powinno dzialac

# start - punkt początkowy
# d - kierunek, wektor, a może nawet i wersor
# beta - wspolczynnik testu
# tauR - początkowa wartość kroku
# epsilon - dokładność odnosząca się do warunku stopu
# function - wpisana przez użytkownika funkcja


def goldstein(start, d, beta, tauR, epsilon, function):
    problem_size = sp.shape(start)[0]  # ilość zmiennych uzależniam od wymiaru punktu startowego, co może nie być najlepszym pomysłem
    if problem_size < 2:
        print("Błąd, za mało zmiennych.")
    if problem_size > 5:
        print("Błąd, za dużo zmiennych.")
    if tauR <= 0:
        print("Błąd, współczynnik kroku nie większy od zera.")
    grad = []
    variables = []
    x1, x2, x3 = sp.symbols('x1 x2 x3')
    fun = sp.cos(x1) + 2*x2**2 - 3*x3
    for i in range(1, problem_size+1):
        variables.append(sp.symbols('x'+str(i)))
    for i in range(0, problem_size):
        grad.append(sp.Derivative(fun, variables[i], evaluate=True))  # Tworzę listę z kolejnych pochodnych cząstkowych
    grad_x = []

    # uwaga tutaj na pewno istnieje prostsze rozwiązanie w pętli, którego próba implementacji w moim wykonaniu nie przyniosła efektu
    for j in range(0, problem_size):
        grad_x.append(str(grad[j]))
    grad01 = 0
    grad02 = 0
    grad03 = 0
    grad04 = 0
    grad05 = 0

    # find szuka w stringu kolejnych zmiennych x1, x2 ... pewnie analogicznie trzeba bedzie napisac interpreter
    # subs podstawia pod dana zmienna dana wartosc
    # evalf() zapisuje wynik numerycznie zamiast sin(3.14) daje okolo 0

    for i in range(1, problem_size + 1):
        if grad_x[0].find('x' + str(i)) > 0:
            grad01 += grad[0].subs('x' + str(i), start[i-1]).evalf()
    for i in range(1, problem_size + 1):
        if grad_x[1].find('x' + str(i)) > 0:
            grad02 += grad[1].subs('x' + str(i), start[i - 1]).evalf()
    if problem_size > 2:
        for i in range(1, problem_size + 1):
            if grad_x[2].find('x' + str(i)) > 0:
                grad03 += grad[2].subs('x' + str(i), start[i - 1]).evalf()
    if problem_size > 3:
        for i in range(1, problem_size + 1):
            if grad_x[3].find('x' + str(i)) > 0:
                grad04 += grad[3].subs('x' + str(i), start[i - 1]).evalf()
    if problem_size > 4:
        for i in range(1, problem_size + 1):
            if grad_x[4].find('x' + str(i)) > 0:
                grad05 += grad[4].subs('x' + str(i), start[i - 1]).evalf()

    if problem_size == 2:
        grad0 = sp.Matrix([grad01, grad02])
    if problem_size == 3:
        grad0 = sp.Matrix([grad01, grad02, grad03])
    if problem_size == 4:
        grad0 = sp.Matrix([grad01, grad02, grad03, grad04])
    if problem_size == 5:
        grad0 = sp.Matrix([grad01, grad02, grad03, grad04, grad05])

    p = grad0.T*d  # p jest skalarem, ale w sympy wynik mnożenia macierzy zawsze jest macierzą, więc to przypisanie jest
    p = p[0]       #  konieczne dla zamierzonego efektu, tu można też dodać obsługę błędu, gdyby p jednak nie było skalarem
                   # otrzymane p jest pochodną w kierunku i jej obliczenie, to pierwszy krok w Goldsteinie
    print(grad0.T)
    print(d)
    print(p)

    print()

    tauL = 0  # tak by wynikało z pokazanego przykładu, nie mam pewności

    replacementstauR = [('x'+ str(i), start[i-1]+tauR*d[i-1]) for i in range(1, problem_size+1)]
    replacements0 = [('x' + str(i), start[i - 1]) for i in range(1, problem_size + 1)]
    # sprawdzenie warunku z kroku 1
    if not fun.subs(replacementstauR).evalf() < fun.subs(replacements0).evalf():
        print("Coś nie tak z tauR lub kierunkiem")

    # krok 2
    tau = 1/2*(tauL+tauR)
    replacementstau = [('x' + str(i), start[i - 1]+tau*d[i-1]) for i in range(1, problem_size + 1)]
    fxtaud = fun.subs(replacementstau).evalf()

    #krok 3
