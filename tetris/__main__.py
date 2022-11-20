from PyQt5.QtWidgets import QApplication
import sys


app = QApplication(sys.argv)
sys.path.append(".")
sys.path.append("./tetris")

from .view.mainWindow.main_window import MainWindow

main_window = MainWindow()
app.exec()
