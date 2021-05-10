from testFunctions import TestFunctions


def getTestFunction(x) -> str:
    return {
        "1": TestFunctions.modified_himmelblau_function(),
        "2": TestFunctions.goldstein_price_function(),
        "3": TestFunctions.geem_function(),
        "4": TestFunctions.test_function(),
    }.get(x, x)


def getFormulaString() -> str:
    print(
        "Enter formula (f.e. 2*x+y**3) or choose formula, where: \n 1 - modified himmelblau function \n 2 - goldstein-price function \n 3 - geem function \n 4 - some test function "
    )
    formula_string = input()
    return getTestFunction(formula_string)
