from errorhandlers.ProblemSizeError import ProblemSizeError


def goldstein_values_exception(problem_size, tauR, beta):
    if not 2 <= problem_size <= 5:
        raise ProblemSizeError("Liczba zmiennych powinna być z przedziału [2, 5].")
    if not tauR > 0:
        raise ProblemSizeError("Współczynnik kroku powinien być większy od zera.")
    if not 0 < beta < 0.5:
        raise ProblemSizeError("Współczynnik testu powinien być z przedziału (0, 0.5).")
