from PyQt5 import QtWidgets
from mydesign import Ui_MainWindow
import sys


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Добавляем новые значения
        self.ui.comboBox.addItem("Программист")
        self.ui.comboBox.addItem("Дизайнер")


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())