# TICTACTOE-game
#This project implements a Tic-Tac-Toe game with an unbeatable Artificial Intelligence (AI) using the Minimax algorithm. The AI ensures optimal play, making it impossible for a player to win unless they make a mistake.

Table of Contents
Overview
Features
Setup Instructions
How to Play
Project Structure
AI Algorithm
License
Overview
The project focuses on creating an intelligent agent that plays Tic-Tac-Toe perfectly. The AI calculates the best possible moves by exploring all future game states using the Minimax algorithm. If both the player and AI play optimally, the game will always end in a tie.

Features
Unbeatable AI opponent powered by the Minimax algorithm
Game logic checks for:
Valid player moves
Winner determination
Tie conditions
Game over state
Interactive user interface powered by Pygame
Supports single-player mode against AI
Setup Instructions
To run the project, follow these steps:

Clone the repository:

bash
Copy code
git clone https://github.com/USERNAME/tictactoe.git
Install the required dependencies: Navigate to the project directory and install the required package:

bash
Copy code
pip install -r requirements.txt
Run the game: Execute the following command to start the game:

bash
Copy code
python runner.py
How to Play
Player 'X' makes the first move.
Click on an empty square to place your move.
The AI (player 'O') will automatically play its move based on the Minimax algorithm.
Continue alternating turns until a player wins or the game ends in a tie.
Project Structure
runner.py: Handles the graphical user interface and game flow.
tictactoe.py: Contains the game logic, including the AI implementation using the Minimax algorithm.
AI Algorithm
The AI is implemented using the Minimax algorithm, a decision-making process that evaluates all possible game states to determine the optimal move. It considers the player’s possible responses to its moves, ensuring that it never loses. The AI either wins or forces a tie, making it unbeatable under optimal play.

License
This project is licensed under the MIT License. See the LICENSE file for details.
