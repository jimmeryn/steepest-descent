from py_expression_eval import Parser
from math import sin

def getSormulaString():
    print('Enter formula (f.e. 2*x+y**3): ')
    formula_string = input()
    return formula_string

class Equation:
    def __init__(self):
        self.parser = Parser()
        while True:
            try:
                formula_string = getSormulaString()
                self.formula = self.parser.parse(formula_string)
                self.variables = self.formula.variables()
                break
            except :
                print("That was no valid formula.")

