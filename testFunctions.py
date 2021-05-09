# Przy parserze sympy lepiej zadawać funkcje stringami


def goldstein_price_function():
    return "(1 + ((x1 + x2 + 1) ** 2) * (19 - 14 * x1 + 3 * x1 ** 2 + 6 * x1 * x2 + 3 * x2 ** 2)) * (30 + ((2 * x1 - 3 * x2) ** 2) * (18 - 32 * x1 + 12 * x1 ** 2 + 48 * x2 - 36 * x1 * x2 + 27 * x2 ** 2))"


def modified_himmelblau_function():
    return "(x1 ** 2 + x2 - 11) ** 2 + (x1 + x2 ** 2 - 7) ** 2 - 200"


def geem_function():
    return "4 * x1 ** 2 - 2.1 * x1 ** 4 + x1 ** 6 / 3 + x1 * x2 - 4 * x2 ** 2 + 4 * x2 ** 4"


def test_function():
    return "(x1 - 2) ** 2 + (x1 - x2 ** 2) ** 2"
