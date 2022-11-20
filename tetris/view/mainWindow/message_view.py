from PyQt5.QtWidgets import QDialog, QPushButton, QLabel
from PyQt5 import uic
from ...UI import message_view_ui


class MessageView(QDialog):
    __confirm_button: QPushButton
    __message_label: QLabel

    def __init__(self, label_text=None):
        super().__init__()
        uic.loadUi(message_view_ui, self)
        self.__setup_ui(
            confirm_button=self.confirmButton, message_label=self.messageLabel
        )
        self.__message_label.setText(label_text)
        self.__confirm_button.clicked.connect(lambda: self.close())

    def __setup_ui(
        self, confirm_button: QPushButton = None, message_label: QLabel = None
    ):
        self.__confirm_button = confirm_button
        self.__message_label = message_label
