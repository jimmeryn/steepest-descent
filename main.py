from goldstein import goldstein
import sympy as sp


def main():
    # nie wiem co zrobilem źle, tutaj przy tauR = 3.5 znajduje wynik po 12 iteracjach, a dla tauR = 3.7 nie znajduje
    goldstein(sp.Matrix([0, 0]), sp.Matrix([1, 0]), 2 / 5, 3.6, 0.001, "atan(x1)+x2**2")


if __name__ == "__main__":
    main()
