from ui.canvas import Canvas
from testFunctions import TestFunctions
from mns import mns
from ui.ui_first_attempt import Ui_MainWindow
from PyQt5 import QtWidgets as qtw
from functionStringParser import function_string_parser


class MainWindow(qtw.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Metoda Najszybszego Spadku")
        self.connectButtons()

    def handleOnStart(self):
        line_func = self.ui.lineEdit_function.text()
        line_iter = self.ui.lineEdit_iteration.text()
        line_start_vec = self.ui.lineEdit_start_vector.text()
        line_step_size = self.ui.lineEdit_step_size.text()
        line_stop_term = self.ui.lineEdit_stop_term.text()
        line_test = self.ui.lineEdit_test.text()
        # mns()
        self.addCanvas(line_func)

    def addCanvas(self, line_func: str):
        func = function_string_parser(line_func)
        sc = Canvas(self, fun=func, width=5, height=4, dpi=100)
        layout = qtw.QVBoxLayout()
        layout.addWidget(sc)
        self.ui.groupBox_3.setLayout(layout)

    def connectButtons(self):
        self.ui.pushButton_start_algorythm.clicked.connect(self.handleOnStart)
        self.ui.pushButton_Geem.clicked.connect(self.handleFunctionGeemButtonClick)
        self.ui.pushButton_Goldstei_Pirce.clicked.connect(self.handleFunctionPriceButtonClick)
        self.ui.pushButton_Himmelblau.clicked.connect(self.handleFunctionHimButtonClick)
        self.ui.pushButton_test_function.clicked.connect(self.handleFunctionTestButtonClick)

    def handleFunctionHimButtonClick(self):
        self.ui.lineEdit_function.setText(TestFunctions.modified_himmelblau_function())

    def handleFunctionPriceButtonClick(self):
        self.ui.lineEdit_function.setText(TestFunctions.goldstein_price_function())

    def handleFunctionGeemButtonClick(self):
        self.ui.lineEdit_function.setText(TestFunctions.geem_function())

    def handleFunctionTestButtonClick(self):
        self.ui.lineEdit_function.setText(TestFunctions.test_function())


if __name__ == "__main__":
    import sys

    app = qtw.QApplication(sys.argv)
    win = qtw.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(win)
    win.show()
    sys.exit(app.exec_())
