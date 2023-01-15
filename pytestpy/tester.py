import os
import numpy as np
import json
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QVBoxLayout,
    QLineEdit,
    QMessageBox,
)
from PyQt5.QtGui import QFont

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        font = QFont()
        font.setPointSize(16)
        self.username_input = QLineEdit()
        self.username_input.setMinimumHeight(100)
        self.username_input.setFont(font)
        self.password_input = QLineEdit()
        self.password_input.setMinimumHeight(100)
        self.password_input.setFont(font)
        self.register_button = QPushButton("Register")
        self.register_button.setMinimumHeight(100)
        self.register_button.setFont(font)
        self.login_button = QPushButton("Log in")
        self.login_button.setMinimumHeight(100)
        self.login_button.setFont(font)
        self.register_button.clicked.connect(self.register)
        self.login_button.clicked.connect(self.login)

        layout = QVBoxLayout()
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_input)
        layout.addWidget(self.register_button)
        layout.addWidget(self.login_button)
        self.setLayout(layout)

        # Set the window size to width=800 and height=600.
        self.resize(800, 600)

        self.setWindowTitle("Login")
        self.show()

    def register(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if len(username) < 4:
            error_message = "The username must be at least 4 characters long."
            QMessageBox.warning(self, "Error", error_message)
            return

        if len(password) < 6:
            error_message = "The password must be at least 6 characters long."
            QMessageBox.warning(self, "Error", error_message)
            return

        fileloc = "information.json"
        with open(fileloc, "w") as file_object:
            account_info = {
                "username": username,
                "password": password,
            }
            json.dump(account_info, file_object)
            QMessageBox.information(self, "Success", "Account registered successfully.")

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        fileloc = "information.json"
        with open(fileloc, "r") as file_object:
            account_info = json.load(file_object)
            if (
                account_info["username"] == username
                and account_info["password"] == password
            ):
                QMessageBox.information(self, "Success", "Login successful.")
            else:
                QMessageBox.warning(
                    self,
                    "Error",
                    "Incorrect username or password. Please try again.",
                )


app = QApplication([])
login_window = LoginWindow()
app.exec_()
