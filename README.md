# Ping Pong Game

A simple Ping Pong game implemented in Python using the Turtle graphics library.

## Description

This project is a basic implementation of the classic Ping Pong game. It features:

- Two-player gameplay
- Score tracking
- Collision detection
- Responsive paddles and ball movement

The game is built using Python and the Turtle graphics library, making it a great project for beginners to understand game development concepts and Python programming.

## Requirements

- Python 3.x
- Turtle graphics library (usually comes pre-installed with Python)

## Installation

1. Clone this repository or download the source code.
2. Ensure you have Python installed on your system.

## How to Play

1. Run the game by executing the following command in your terminal:
   ```
   python main.py
   ```
2. Use the following controls:
   - Left paddle: 'W' (up) and 'S' (down)
   - Right paddle: Up Arrow (up) and Down Arrow (down)
3. The ball will start moving automatically.
4. Each time a player misses the ball, the opponent scores a point.
5. The game continues until you choose to exit.

## Game Features

- **Paddle Movement**: Both players can move their paddles up and down to hit the ball.
- **Ball Movement**: The ball moves across the screen, bouncing off the top and bottom edges.
- **Scoring**: Points are awarded when a player fails to return the ball.
- **Collision Detection**: The game detects collisions between the ball and paddles, as well as the screen boundaries.
- **Restart Option**: After each round, players can choose to start a new game or exit.

## Code Structure

- `main.py`: Contains the main game logic and classes.
- `ScoreBoard`: Manages and displays the game score.
- `PingPongGame`: The main game class that handles the game setup, loop, and mechanics.

## Customization

Feel free to modify the game constants in the `main.py` file to change aspects like screen size, paddle size, ball speed, etc.