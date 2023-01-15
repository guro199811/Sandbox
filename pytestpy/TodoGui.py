import sys

from PyQt5.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit, QListWidget,
QPushButton, QWidget)

class TodoApp(QWidget):
    def __init__(self, todo=None, parent=None):
        super().__init__(parent)

        # Store the to-do list as an instance variable
        self.todo = todo or []

        # Create the UI elements
        self.label = QLabel("To-Do List")
        self.add_button = QPushButton("Add Task")
        self.remove_button = QPushButton("Remove Task")
        self.list_button = QPushButton("List Tasks")
        self.exit_button = QPushButton("Exit")
        self.task_entry = QLineEdit()
        self.task_list = QListWidget()

        # Set up the layout
        layout = QGridLayout()
        layout.addWidget(self.label, 0, 0)
        layout.addWidget(self.task_entry, 1, 0)
        layout.addWidget(self.add_button, 2, 0)
        layout.addWidget(self.remove_button, 3, 0)
        layout.addWidget(self.list_button, 4, 0)
        layout.addWidget(self.exit_button, 5, 0)
        layout.addWidget(self.task_list, 1, 1, 5, 1)
        self.setLayout(layout)

        # Connect the buttons to the appropriate methods
        self.add_button.clicked.connect(self.add_task)
        self.remove_button.clicked.connect(self.remove_task)
        self.list_button.clicked.connect(self.list_tasks)
        self.exit_button.clicked.connect(self.close)

    def add_task(self):
        task = self.task_entry.text()
        self.todo.append(task)
        self.task_list.clear()
        for i, task in enumerate(self.todo):
            self.task_list.addItem(f"{i + 1}: {task}")
        self.task_entry.clear()

    def remove_task(self):
        index = self.task_list.currentRow()
        self.todo.pop(index)
        self.task_list.takeItem(index)
        self.task_list.clear()
        for i, task in enumerate(self.todo):
            self.task_list.addItem(f"{i + 1}: {task}")
        self.task_list.takeItem(index)

    def list_tasks(self):
        self.task_list.clear()
        for i, task in enumerate(self.todo):
            self.task_list.addItem(f"{i + 1}: {task}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TodoApp()
    window.show()
    sys.exit(app.exec_())
