from PyQt5.QtWidgets import QApplication
from view.main_window import MainWindow

if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    app.exec()
