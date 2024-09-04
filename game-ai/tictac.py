from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QPushButton, QWidget, QMessageBox
import sys
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
import psutil


class TicTacToe:
    def __init__(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.current_player = 1

    def reset(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.current_player = 1

    def make_move(self, row, col):
        if self.board[row, col] == 0:
            self.board[row, col] = self.current_player
            self.current_player = -self.current_player
            return True
        return False

    def check_winner(self):
        for i in range(3):
            if np.all(self.board[i, :] == self.current_player) or np.all(self.board[:, i] == self.current_player):
                return self.current_player
        if self.board[0, 0] == self.current_player and self.board[1, 1] == self.current_player and self.board[2, 2] == self.current_player:
            return self.current_player
        if self.board[0, 2] == self.current_player and self.board[1, 1] == self.current_player and self.board[2, 0] == self.current_player:
            return self.current_player
        if np.all(self.board != 0):
            return 0
        return None

    def get_state(self):
        return self.board.flatten()

    def available_moves(self):
        return [(i, j) for i in range(3) for j in range(3) if self.board[i, j] == 0]

    def render(self):
        for row in self.board:
            print(' '.join([str(x) for x in row]))
        print()


class TicTacToeNet(nn.Module):
    def __init__(self):
        super(TicTacToeNet, self).__init__()
        self.fc1 = nn.Linear(9, 128)
        self.fc2 = nn.Linear(128, 128)
        self.fc3 = nn.Linear(128, 9)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x


def get_system_usage():
    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory().percent
    return cpu_percent, memory_percent


game = TicTacToe()
model = TicTacToeNet()
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)


def train(game, model, criterion, optimizer, epochs=5000):
    gamma = 0.9
    epsilon = 0.1

    records = []

    for epoch in range(epochs):
        game.reset()
        state = torch.tensor(
            game.get_state(), dtype=torch.float32).unsqueeze(0)
        done = False

        while not done:
            if np.random.rand() < epsilon:
                available_moves = game.available_moves()
                move_idx = np.random.choice(len(available_moves))
                row, col = available_moves[move_idx]
            else:
                with torch.no_grad():
                    output = model(state)
                move = torch.argmax(output).item()
                row, col = divmod(move, 3)

            if game.make_move(row, col):
                reward = 0
                winner = game.check_winner()
                if winner is not None:
                    if winner == 1:
                        reward = 1
                    elif winner == -1:
                        reward = -1
                    done = True

                new_state = torch.tensor(
                    game.get_state(), dtype=torch.float32).unsqueeze(0)
                target = reward
                if not done:
                    with torch.no_grad():
                        target += gamma * torch.max(model(new_state)).item()

                output = model(state)
                target_f = output.clone()
                move = row * 3 + col
                target_f[0][move] = target
                optimizer.zero_grad()
                loss = criterion(output, target_f)
                loss.backward()
                optimizer.step()

                state_list = state.tolist()
                records.append({
                    "epoch": epoch,
                    "state": state_list,
                    "move": move,
                    "reward": reward,
                    "output": output.detach().numpy().flatten(),
                    "target": target_f.detach().numpy().flatten()
                })

                state = new_state

    df = pd.DataFrame(records)
    df.to_csv('tictactoe_training_ia.csv', index=False)
    torch.save(model.state_dict(), 'tictactoe_model.pth')


train(game, model, criterion, optimizer)


def ai_move(game, model):
    state = torch.tensor(game.get_state(), dtype=torch.float32).unsqueeze(0)
    with torch.no_grad():
        output = model(state)
    valid_moves = game.available_moves()
    move = None

    while move is None:
        candidate_move = torch.argmax(output).item()
        row, col = divmod(candidate_move, 3)
        if (row, col) in valid_moves:
            move = candidate_move
        else:
            output[0][candidate_move] = float('-inf')

    row, col = divmod(move, 3)
    game.make_move(row, col)


class TicTacToeGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic Tac Toe")
        self.setFixedSize(QSize(300, 300))

        self.game = TicTacToe()
        self.model = TicTacToeNet()
        self.model.load_state_dict(torch.load("tictactoe_model.pth"))
        self.model.eval()

        self.initUI()

    def initUI(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.grid_layout = QGridLayout()
        self.central_widget.setLayout(self.grid_layout)

        self.buttons = {}
        for row in range(3):
            for col in range(3):
                button = QPushButton("")
                button.setFixedSize(QSize(100, 100))
                button.clicked.connect(self.make_move)
                self.grid_layout.addWidget(button, row, col)
                self.buttons[(row, col)] = button

    def make_move(self):
        button = self.sender()
        index = self.grid_layout.indexOf(button)  # type: ignore
        row, col = divmod(index, 3)

        if self.game.board[row, col] != 0:
            return

        self.game.make_move(row, col)
        self.update_board()

        winner = self.game.check_winner()
        if winner is not None:
            self.show_winner(winner)
            return

        self.ai_move()
        self.update_board()

        winner = self.game.check_winner()
        if winner is not None:
            self.show_winner(winner)

    def ai_move(self):
        state = torch.tensor(self.game.get_state(),
                             dtype=torch.float32).unsqueeze(0)
        with torch.no_grad():
            output = self.model(state)
        valid_moves = self.game.available_moves()
        move = None

        while move is None:
            candidate_move = torch.argmax(output).item()
            row, col = divmod(candidate_move, 3)
            if (row, col) in valid_moves:
                move = candidate_move
            else:
                output[0][candidate_move] = float('-inf')

        row, col = divmod(move, 3)
        self.game.make_move(row, col)

    def update_board(self):
        for (row, col), button in self.buttons.items():
            if self.game.board[row, col] == 1:
                button.setText("X")
            elif self.game.board[row, col] == -1:
                button.setText("O")
            else:
                button.setText("")

    def show_winner(self, winner):
        msg = QMessageBox()
        if winner == 0:
            msg.setText("It's a tie!")
        else:
            msg.setText(f"Player {'1' if winner == 1 else '2'} wins!")
        msg.exec_()
        self.game.reset()
        self.update_board()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TicTacToeGUI()
    window.show()
    sys.exit(app.exec_())
