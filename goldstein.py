import sympy as sp

# Wstępnie rozpisze goldsteina jako pojedyncza funkcje i potem ewentualnie to sie jakos rozbije
# bo jeszcze sam do konca nie jestem pewien jak to powinno dzialac

# start - punkt początkowy
# d - kierunek będący wektorem
# beta - wspolczynnik testu
# tauR - początkowa wartość kroku
# function - wpisana przez użytkownika funkcja, to trzeba dostosować do parsera
# w źródłach pojawia się jeszcze dokładność, ale brak miejsca na jego zastosowanie,
# możliwe ze w dalszej implementacji będzie potrzebny


def goldstein(start, d, beta, tauR, function):
    problem_size = sp.shape(start)[0]  # ilość zmiennych uzależniam od wymiaru punktu startowego

    # poniższe warunki są konieczne i trzeba do nich rozpisać obsługę błędów, niekoniecznie w tym pliku
    if problem_size < 2:
        print("Błąd, za mało zmiennych.")
    if problem_size > 5:
        print("Błąd, za dużo zmiennych.")
    if tauR <= 0:
        print("Błąd, współczynnik kroku nie większy od zera.")
    if beta >= 1 or beta <= 0:
        print("Błąd, współczynnik testu powinien być między 0, a 1")

    grad = []  # gradient na symbolach, lista w praktyce zawierająca między 2, a 5 elementów
    variables = []  # lista zmiennych wstepnie bym przyjął zgodnie z konwencją x1, x2, x3...

    # statyczne zaimplementowanie zmiennych symbolicznych, jeśli utrzymamy konwencję będzie dobrym rozwiązaniem
    x1, x2, x3, x4, x5 = sp.symbols('x1 x2 x3 x4 x5')
    # poniżej test, w tym miejscu trzeba odpowiednio podstawić function pod fun
    fun = x1**2 + 2*x2**2 - 6*x1 + x1*x2

    #krok 1
    # na listę zmiennych wrzucamy kolejne zmienne zależnie od rozmiaru zadania
    for i in range(1, problem_size+1):
        variables.append(sp.symbols('x'+str(i)))
    for i in range(0, problem_size):
        grad.append(sp.Derivative(fun, variables[i], evaluate=True))  # Tworzę listę z kolejnych pochodnych cząstkowych

    # zasadniczo niepotrzebne, ale pozwoli uniknąć błędów na poziomie testów
    grad03 = 0
    grad04 = 0
    grad05 = 0

    # wektor zastąpień do metody subs, robi robote
    replacements0 = [('x' + str(i), start[i - 1]) for i in range(1, problem_size + 1)]

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

    p = grad0.T*d  # p jest skalarem, ale w sympy wynik mnożenia macierzy zawsze jest macierzą, więc to przypisanie jest
    p = p[0]       #  konieczne dla zamierzonego efektu, tu można też dodać obsługę błędu, gdyby p jednak nie było skalarem
                   # otrzymane p jest pochodną w kierunku i jej obliczenie, to pierwszy krok w Goldsteinie

    tauL = 0  # tak by wynikało z pokazanego przykładu, nie mam pewności

    replacementstauR = [('x'+ str(i), start[i-1] + tauR * d[i-1]) for i in range(1, problem_size+1)]

    # sprawdzenie warunku
    if not fun.subs(replacementstauR).evalf() < fun.subs(replacements0).evalf():
        print("Warunek (1) nie zachodzi")

    # poniżej główna pętla algorytmu, bez większej filozofii, zgodnie ze źródłami
    # krok 2
    while True:
        tau = 1/2*(tauL+tauR)
        replacementstau = [('x' + str(i), start[i - 1]+tau*d[i-1]) for i in range(1, problem_size + 1)]
        fxtaud = fun.subs(replacementstau).evalf()

        # krok 3
        if fxtaud < fun.subs(replacements0).evalf() + (1-beta)*p*tau:
            tauL = tau
        # krok 4
        elif fxtaud > fun.subs(replacements0).evalf() + beta*p*tau:
            tauR = tau
        else:
            print(tau)  # test
            return tau