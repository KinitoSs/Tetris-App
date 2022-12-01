import sys

from PyQt5.QtWidgets import QApplication
from rich.traceback import install

from .view.mainWindow.main_window import MainWindow

install(show_locals=True)

app = QApplication(sys.argv)
sys.path.append(".")
sys.path.append("./tetris")

main_window = MainWindow()
app.exec()
sys.exit()
