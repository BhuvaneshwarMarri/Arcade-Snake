import tkinter as tk
import random

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        self.root.geometry("400x400")

        self.canvas = tk.Canvas(root, bg="black", width=400, height=400)
        self.canvas.pack()

        self.snake = [(100, 100), (90, 100), (80, 100)]
        self.direction = "Right"
        self.food_position = self.create_food()
        self.score = 0  # Initialize score

        self.root.bind("<KeyPress>", self.on_key_press)
        self.root.bind("<space>", self.restart_game)

        self.update_game()

    def create_food(self):
        x = random.randint(1, 19) * 20
        y = random.randint(1, 19) * 20
        self.canvas.create_rectangle(x, y, x + 20, y + 20, fill="red", tags="food")
        return x, y

    def move_snake(self):
        head = self.snake[0]
        if self.direction == "Right":
            new_head = (head[0] + 20, head[1])
        elif self.direction == "Left":
            new_head = (head[0] - 20, head[1])
        elif self.direction == "Up":
            new_head = (head[0], head[1] - 20)
        elif self.direction == "Down":
            new_head = (head[0], head[1] + 20)

        self.snake = [new_head] + self.snake[:-1]

    def check_collision(self):
        head = self.snake[0]

        # Check if the snake collides with itself
        if head in self.snake[1:]:
            return True

        # Check if the snake collides with the walls
        if head[0] < 0 or head[0] >= 400 or head[1] < 0 or head[1] >= 400:
            return True

        return False

    def check_food_collision(self):
        head = self.snake[0]
        food = self.canvas.coords("food")
        
        if len(food)>0 and head[0] == food[0] and head[1] == food[1]:
            self.snake.append((0, 0))
            self.canvas.delete("food")
            self.food_position = self.create_food()
            self.score += 1  # Increase score

    def update_game(self):
        food = self.canvas.coords("food")
        if len(food)<=0:
            self.create_food()
            
        self.move_snake()

        if self.check_collision():
            self.canvas.create_text(
                200, 200, text=f"Game Over.\n  Score: {self.score}.\nPress Space to Restart",
                fill="white", font=("Helvetica", 16), tags="game_over"
            )
            return

        self.check_food_collision()

        self.canvas.delete("snake")
        for segment in self.snake:
            self.canvas.create_rectangle(
                segment[0], segment[1], segment[0] + 20, segment[1] + 20, fill="green", tags="snake"
            )

        self.root.after(100, self.update_game)

    def on_key_press(self, event):
        if event.keysym == "Up" and self.direction != "Down":
            self.direction = "Up"
        elif event.keysym == "Down" and self.direction != "Up":
            self.direction = "Down"
        elif event.keysym == "Left" and self.direction != "Right":
            self.direction = "Left"
        elif event.keysym == "Right" and self.direction != "Left":
            self.direction = "Right"

    def restart_game(self, event):
        self.snake = [(100, 100), (90, 100), (80, 100)]
        self.direction = "Right"
        self.food_position = self.create_food()
        self.score = 0  # Reset score
        self.canvas.delete("snake")
        self.canvas.delete("game_over")
        self.canvas.delete("food")# Delete the game over text
        self.update_game()

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
