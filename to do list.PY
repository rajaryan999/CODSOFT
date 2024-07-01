import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget, QLineEdit, QMessageBox, QLabel, QFrame
)
from PyQt5.QtGui import QFont, QIcon, QColor
from PyQt5.QtCore import Qt

class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set window properties
        self.setGeometry(300, 300, 500, 600)
        self.setWindowTitle('To-Do List')
        self.setWindowIcon(QIcon('todo_icon.png'))
        self.setStyleSheet("background-color: #f0f0f0;")

        # Main layout
        main_layout = QVBoxLayout()

        # Title
        title = QLabel('My To-Do List')
        title.setFont(QFont('Arial', 28))
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: #4a4a4a; margin-bottom: 20px;")
        main_layout.addWidget(title)

        # Task input layout
        input_layout = QHBoxLayout()
        self.task_input = QLineEdit(self)
        self.task_input.setFont(QFont('Arial', 16))
        self.task_input.setPlaceholderText("Enter a new task")
        self.task_input.setStyleSheet("padding: 10px; border: 2px solid #4a90e2; border-radius: 5px;")
        input_layout.addWidget(self.task_input)

        # Buttons
        buttons_layout = QVBoxLayout()
        buttons_layout.setSpacing(10)

        add_button = QPushButton('Add Task', self)
        add_button.setFont(QFont('Arial', 14))
        add_button.setStyleSheet("background-color: #4a90e2; color: white; padding: 10px; border-radius: 5px;")
        add_button.clicked.connect(self.add_task)
        buttons_layout.addWidget(add_button)

        update_button = QPushButton('Update Task', self)
        update_button.setFont(QFont('Arial', 14))
        update_button.setStyleSheet("background-color: #f5a623; color: white; padding: 10px; border-radius: 5px;")
        update_button.clicked.connect(self.update_task)
        buttons_layout.addWidget(update_button)

        delete_button = QPushButton('Delete Task', self)
        delete_button.setFont(QFont('Arial', 14))
        delete_button.setStyleSheet("background-color: #d0021b; color: white; padding: 10px; border-radius: 5px;")
        delete_button.clicked.connect(self.delete_task)
        buttons_layout.addWidget(delete_button)

        input_layout.addLayout(buttons_layout)
        main_layout.addLayout(input_layout)

        # Separator
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        separator.setStyleSheet("color: #c0c0c0; margin-top: 20px; margin-bottom: 20px;")
        main_layout.addWidget(separator)

        # Task list
        self.task_list = QListWidget(self)
        self.task_list.setFont(QFont('Arial', 16))
        self.task_list.setStyleSheet("padding: 10px; border: 2px solid #4a90e2; border-radius: 5px;")
        main_layout.addWidget(self.task_list)

        # Set main layout
        self.setLayout(main_layout)

    def add_task(self):
        task = self.task_input.text().strip()
        if task:
            self.task_list.addItem(task)
            self.task_input.clear()
        else:
            QMessageBox.warning(self, 'Warning', 'Task cannot be empty')

    def update_task(self):
        current_row = self.task_list.currentRow()
        task = self.task_input.text().strip()
        if current_row >= 0 and task:
            self.task_list.takeItem(current_row)
            self.task_list.insertItem(current_row, task)
            self.task_input.clear()
        else:
            QMessageBox.warning(self, 'Warning', 'No task selected or task is empty')

    def delete_task(self):
        current_row = self.task_list.currentRow()
        if current_row >= 0:
            self.task_list.takeItem(current_row)
        else:
            QMessageBox.warning(self, 'Warning', 'No task selected')

def main():
    app = QApplication(sys.argv)
    todo_app = ToDoApp()
    todo_app.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
