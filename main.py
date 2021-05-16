import sys
from PyQt5 import QtWidgets
from ui.ui import MainWindow as UiWindow


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    win = UiWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
