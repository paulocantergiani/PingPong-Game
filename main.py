# Import required modules
from turtle import Turtle, Screen
import time

# Define constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PANEL_SIZE = 10
MOVE_DISTANCE = 10
TIME_DELAY = 0.008
FONT = ("Courier", 24, "normal")


# ScoreBoard class to keep track and display scores
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_score()

    # Update and display the current score
    def update_score(self):
        self.clear()
        self.goto(-100, SCREEN_HEIGHT // 2 - 40)
        self.write(self.left_score, align="center", font=FONT)
        self.goto(100, SCREEN_HEIGHT // 2 - 40)
        self.write(self.right_score, align="center", font=FONT)

    # Increment left player's score
    def left_point(self):
        self.left_score += 1
        self.update_score()

    # Increment right player's score
    def right_point(self):
        self.right_score += 1
        self.update_score()


# Main game class
class PingPongGame:
    def __init__(self):
        self.screen = self.setup_screen()
        self.panels = self.setup_panels()
        self.ball = self.setup_ball()
        self.scoreboard = ScoreBoard()
        self.ball_direction = "Up and Right"
        self.keys_pressed = {"Up": False, "Down": False, "w": False, "s": False}
        self.setup_controls()

    # Set up the game screen
    def setup_screen(self):
        screen = Screen()
        screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        screen.bgcolor("black")
        screen.title("Ping Pong")
        screen.tracer(0)
        return screen

    # Create the paddles (panels) for both players
    def setup_panels(self):
        left_panel = []
        right_panel = []

        # Create left panel
        for i in range(PANEL_SIZE):
            panel = Turtle("square")
            panel.color("white")
            panel.penup()
            panel.goto(-SCREEN_WIDTH // 2 + 20, (i * 20) - (PANEL_SIZE * 10))
            left_panel.append(panel)

        # Create right panel
        for i in range(PANEL_SIZE):
            panel = Turtle("square")
            panel.color("white")
            panel.penup()
            panel.goto(SCREEN_WIDTH // 2 - 20, (i * 20) - (PANEL_SIZE * 10))
            right_panel.append(panel)

        return left_panel, right_panel

    # Create the ball
    def setup_ball(self):
        ball = Turtle("circle")
        ball.color("white")
        ball.penup()
        return ball

    # Move the panels based on key presses
    def move_panel(self):
        if (self.keys_pressed["Up"] == True) and (
            self.panels[1][-1].ycor() < SCREEN_HEIGHT // 2
        ):
            for segment in self.panels[1]:
                segment.goto(segment.position() + (0, MOVE_DISTANCE))
        elif (self.keys_pressed["Down"] == True) and (
            self.panels[1][0].ycor() > -SCREEN_HEIGHT // 2
        ):
            for segment in self.panels[1]:
                segment.goto(segment.position() - (0, MOVE_DISTANCE))
        elif (self.keys_pressed["w"] == True) and (
            self.panels[0][-1].ycor() < SCREEN_HEIGHT // 2
        ):
            for segment in self.panels[0]:
                segment.goto(segment.position() + (0, MOVE_DISTANCE))
        elif (self.keys_pressed["s"] == True) and (
            self.panels[0][0].ycor() > -SCREEN_HEIGHT // 2
        ):
            for segment in self.panels[0]:
                segment.goto(segment.position() - (0, MOVE_DISTANCE))
        else:
            self.keys_pressed = {"Up": False, "Down": False, "w": False, "s": False}

    # Reset all keys to not pressed
    def reset_keys(self):
        self.keys_pressed = {"Up": False, "Down": False, "w": False, "s": False}

    # Set the respective key as pressed for panel movement
    def move_up_right_panel(self):
        self.keys_pressed["Up"] = True

    def move_down_right_panel(self):
        self.keys_pressed["Down"] = True

    def move_up_left_panel(self):
        self.keys_pressed["w"] = True

    def move_down_left_panel(self):
        self.keys_pressed["s"] = True

    # Move the ball based on its current direction
    def ball_movement(self):
        if self.ball_direction == "Up and Right":
            self.ball.goto(self.ball.position() + (4, 2))
        elif self.ball_direction == "Down and Right":
            self.ball.goto(self.ball.position() + (4, -2))
        elif self.ball_direction == "Up and Left":
            self.ball.goto(self.ball.position() + (-4, 2))
        elif self.ball_direction == "Down and Left":
            self.ball.goto(self.ball.position() + (-4, -2))

    # Set up key bindings for panel movement
    def setup_controls(self):
        self.screen.listen()
        self.screen.onkeypress(lambda: self.move_up_right_panel(), "Up")
        self.screen.onkeyrelease(lambda: self.reset_keys(), "Up")
        self.screen.onkeypress(lambda: self.move_down_right_panel(), "Down")
        self.screen.onkeyrelease(lambda: self.reset_keys(), "Down")
        self.screen.onkeypress(lambda: self.move_up_left_panel(), "w")
        self.screen.onkeyrelease(lambda: self.reset_keys(), "w")
        self.screen.onkeypress(lambda: self.move_down_left_panel(), "s")
        self.screen.onkeyrelease(lambda: self.reset_keys(), "s")

    # Check for collisions between the ball and panels or screen edges
    def check_collision(self):
        if (
            self.ball.xcor() > SCREEN_WIDTH // 2 - 40
            or self.ball.xcor() < -SCREEN_WIDTH // 2 + 40
        ) and (self.panels[0][0].ycor() < self.ball.ycor() < self.panels[0][-1].ycor()
            or self.panels[1][0].ycor() < self.ball.ycor() < self.panels[1][-1].ycor()) :
            if self.ball_direction == "Up and Right":
                self.ball_direction = "Up and Left"
                self.scoreboard.right_point()
                return
            elif self.ball_direction == "Down and Right":
                self.ball_direction = "Down and Left"
                self.scoreboard.right_point()
                return
            elif self.ball_direction == "Up and Left":
                self.ball_direction = "Up and Right"
                self.scoreboard.left_point()
                return
            elif self.ball_direction == "Down and Left":
                self.ball_direction = "Down and Right"
                self.scoreboard.left_point()
                return
        if (
            self.ball.ycor() > SCREEN_HEIGHT // 2 - 10
            or self.ball.ycor() < -SCREEN_HEIGHT // 2 + 10
        ):
            if self.ball_direction == "Up and Right":
                self.ball_direction = "Down and Right"
                return
            elif self.ball_direction == "Down and Right":
                self.ball_direction = "Up and Right"
                return
            elif self.ball_direction == "Up and Left":
                self.ball_direction = "Down and Left"
                return
            elif self.ball_direction == "Down and Left":
                self.ball_direction = "Up and Left"
                return

    # Check if the ball has gone out of bounds (game over condition)
    def check_gameover(self):
        if (
            self.ball.xcor() > SCREEN_WIDTH // 2 - 10
            or self.ball.xcor() < -SCREEN_WIDTH // 2 + 10
        ):
            return True
        return False

    # Reset the ball position and direction for a new game
    def reset_game(self):
        self.ball.goto(0, 0)
        self.ball_direction = "Up and Right"

    # Main game loop
    def game_loop(self):
        while True:
            self.move_panel()
            self.ball_movement()
            self.check_collision()
            if self.check_gameover():
                answer = self.screen.textinput(
                    "Game Over",
                    f"The score was: Left: {self.scoreboard.left_score} and Right: {self.scoreboard.right_score}. Would you like to play again? (Yes/No): ",
                )
                if answer.lower() == "yes":
                    self.reset_game()
                    self.setup_controls()
                else:
                    break
            self.screen.update()
            time.sleep(TIME_DELAY)

    # Run the game
    def run(self):
        self.game_loop()
        self.screen.exitonclick()


# If this script is run directly, create and run the game
if __name__ == "__main__":
    game = PingPongGame()
    game.run()
