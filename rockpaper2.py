import random
from PyQt5 import QtWidgets, QtGui, QtCore

# Define the choices
choices = ["Rock", "Paper", "Scissors"]

class RockPaperScissors(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.user_score = 0
        self.computer_score = 0
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Rock-Paper-Scissors Game")
        self.setGeometry(400, 400, 400, 400)
        self.setStyleSheet("background-color: #3498DB;")
        self.setFixedSize(700, 500)

        layout = QtWidgets.QVBoxLayout()

        title_label = QtWidgets.QLabel("Rock-Paper-Scissors", self)
        title_label.setFont(QtGui.QFont('Helvetica', 24, QtGui.QFont.Bold))
        title_label.setStyleSheet("color: #FFFFFF;")
        title_label.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(title_label)
        
        self.result_text = QtWidgets.QLabel("", self)
        self.result_text.setFont(QtGui.QFont('Helvetica', 16))
        self.result_text.setStyleSheet("color: #FFFFFF;")
        self.result_text.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(self.result_text)
        
        self.score_text = QtWidgets.QLabel(f"User: {self.user_score} | Computer: {self.computer_score}", self)
        self.score_text.setFont(QtGui.QFont('Helvetica', 16))
        self.score_text.setStyleSheet("color: #FFFFFF;")
        self.score_text.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(self.score_text)

        button_layout = QtWidgets.QHBoxLayout()

        rock_button = QtWidgets.QPushButton("Rock", self)
        rock_button.setFont(QtGui.QFont('Helvetica', 12, QtGui.QFont.Bold))
        rock_button.setStyleSheet("background-color: #E74C3C; color: #FFFFFF;")
        rock_button.clicked.connect(lambda: self.play("Rock"))
        button_layout.addWidget(rock_button)

        paper_button = QtWidgets.QPushButton("Paper", self)
        paper_button.setFont(QtGui.QFont('Helvetica', 12, QtGui.QFont.Bold))
        paper_button.setStyleSheet("background-color: #F1C40F; color: #FFFFFF;")
        paper_button.clicked.connect(lambda: self.play("Paper"))
        button_layout.addWidget(paper_button)

        scissors_button = QtWidgets.QPushButton("Scissors", self)
        scissors_button.setFont(QtGui.QFont('Helvetica', 12, QtGui.QFont.Bold))
        scissors_button.setStyleSheet("background-color: #2ECC71; color: #FFFFFF;")
        scissors_button.clicked.connect(lambda: self.play("Scissors"))
        button_layout.addWidget(scissors_button)

        layout.addLayout(button_layout)

        play_again_button = QtWidgets.QPushButton("Play Again", self)
        play_again_button.setFont(QtGui.QFont('Helvetica', 14, QtGui.QFont.Bold))
        play_again_button.setStyleSheet("background-color: #2980B9; color: #FFFFFF;")
        play_again_button.clicked.connect(self.reset_game)
        layout.addWidget(play_again_button)

        self.setLayout(layout)

    def play(self, user_choice):
        computer_choice = random.choice(choices)
        result = self.determine_winner(user_choice, computer_choice)
        
        self.result_text.setText(f"User: {user_choice} | Computer: {computer_choice}\n{result}")
        self.score_text.setText(f"User: {self.user_score} | Computer: {self.computer_score}")

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Scissors" and computer_choice == "Paper") or \
             (user_choice == "Paper" and computer_choice == "Rock"):
            self.user_score += 1
            return "You win!"
        else:
            self.computer_score += 1
            return "You lose!"

    def reset_game(self):
        self.result_text.setText("")
        self.user_score = 0
        self.computer_score = 0
        self.score_text.setText(f"User: {self.user_score} | Computer: {self.computer_score}")

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    game = RockPaperScissors()
    game.show()
    sys.exit(app.exec_())
