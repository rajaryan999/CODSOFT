import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QGridLayout
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set window properties
        self.setGeometry(300, 300, 400, 500)
        self.setWindowTitle('Simple Calculator')
        self.setWindowIcon(QIcon('calculator_icon.png'))

        # Create display
        self.display = QLineEdit(self)
        self.display.setFont(QFont('Arial', 24))
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.display.setFixedHeight(50)

        # Create grid layout for buttons
        grid = QGridLayout()
        grid.setSpacing(10)

        # Add display to the layout
        grid.addWidget(self.display, 0, 0, 1, 4)

        # Button labels
        buttons = [
            ('AC', 1, 0), ('%', 1, 1), ('Back', 1, 2), ('/', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('0', 5, 0), ('00', 5, 1), ('.', 5, 2), ('=', 5, 3)
        ]

        # Create buttons and add to grid
        for text, row, col, rowspan in [(t[0], t[1], t[2], t[3] if len(t) > 3 else 1) for t in buttons]:
            button = QPushButton(text, self)
            button.setFont(QFont('Arial', 18))
            button.setFixedHeight(60)
            button.clicked.connect(self.on_button_click)
            grid.addWidget(button, row, col, rowspan, 1)

        # Set layout
        self.setLayout(grid)

    def on_button_click(self):
        sender = self.sender().text()

        if sender == '=':
            try:
                expression = self.display.text()
                if '%' in expression:
                    expression = expression.replace('%', '/100')
                result = eval(expression)
                self.display.setText(str(result))
            except Exception as e:
                QMessageBox.critical(self, 'Error', 'Invalid input')
                self.display.setText('')
        elif sender == 'AC':
            self.display.setText('')
        elif sender == 'Back':
            current_text = self.display.text()
            self.display.setText(current_text[:-1])
        else:
            self.display.setText(self.display.text() + sender)

def main():
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
