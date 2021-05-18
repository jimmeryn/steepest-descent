import sympy as sp


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
