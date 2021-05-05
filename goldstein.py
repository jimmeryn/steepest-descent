from sympy import Derivative, lambdify, symbols, sin, cos
from numpy import zeros, matrix, arange

# Wstępnie rozpisze goldsteina jako pojedyncza funkcje i potem ewentualnie to sie jakos rozbije
# bo jeszcze sam do konca nie jestem pewien jak to powinno dzialac

# start - punkt początkowy
# d - kierunek, wektor, a może nawet i wersor
# beta - wspolczynnik testu
# step - początkowa wartość kroku
# epsilon - dokładność odnosząca się do warunku stopu
# function - wpisana przez użytkownika funkcja


def goldstein(start, d, beta, step, epsilon, function):
    problem_size = start.size  # ilość zmiennych uzależniam od wymiaru punktu startowego, co może nie być najlepszym pomysłem
    grad = []
    variables = []
    x1, x2, x3 = symbols('x1 x2 x3')
    fun = cos(x1) + 2*x2**2 - 3*x3
    for i in range(1, problem_size+1):
        variables.append(symbols('x'+str(i)))
    for i in range(0, problem_size):
       grad.append(Derivative(fun, variables[i], evaluate=True))  # takie liczenie gradientu powinno zadzialac

    d = matrix(d).T  # żeby wymnożyć zamieniam kierunek na wektor kolumnowy, bo wstepnie zakladam, ze bedziemy go dawać wierszowo
    f = lambdify(variables, fun)  # to zamienia ten wzorek z ładnymi zmiennymi, na taki zrozumiały dla pythona

    print(d)
    print(f(3.14,1,0))
    print(fun)
    print(grad)
    print(variables)
