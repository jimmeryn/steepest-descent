from ui.ui_first_attempt import Ui_MainWindow
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

class MainWindow(qtw.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Metoda Najszybszego Spadku")

if __name__ == "__main__":
    import sys
    app = qtw.QApplication(sys.argv)
    win = qtw.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(win)
    win.show()
    sys.exit(app.exec_())