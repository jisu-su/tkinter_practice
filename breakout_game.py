import tkinter as tk
import random

# 게임 설정
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 20
BALL_SIZE = 20
BRICK_WIDTH = 75
BRICK_HEIGHT = 30
BRICK_ROWS = 5
BRICK_COLUMNS = 10
BRICK_DROP_SPEED = 0.05  # 벽돌이 내려오는 속도

# 클래스 정의하기
class BreakoutGame:
    def __init__(self, root):
        self.root = root
        self.root.title("벽돌깨기 게임") # 게임 이름
        self.canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="black") # 창 설정
        self.canvas.pack()

        # 패들 생성
        self.paddle = self.canvas.create_rectangle(
            (WINDOW_WIDTH - PADDLE_WIDTH) / 2, WINDOW_HEIGHT - PADDLE_HEIGHT - 10,
            (WINDOW_WIDTH + PADDLE_WIDTH) / 2, WINDOW_HEIGHT - 10,
            fill="white"
        )

        # 공 생성
        self.ball = self.canvas.create_oval(
            (WINDOW_WIDTH - BALL_SIZE) / 2, (WINDOW_HEIGHT - BALL_SIZE) / 2,
            (WINDOW_WIDTH + BALL_SIZE) / 2, (WINDOW_HEIGHT + BALL_SIZE) / 2,
            fill="red"
        )
        self.ball_dx = 4
        self.ball_dy = -4

        # 벽돌 생성
        self.bricks = []
        self.create_bricks()

        # 마우스 이벤트 바인딩
        self.canvas.bind("<Motion>", self.move_paddle)

        # 게임 루프 시작
        self.update_game()

    def create_bricks(self):
        for row in range(BRICK_ROWS):
            for col in range(BRICK_COLUMNS):
                x1 = col * BRICK_WIDTH + 5
                y1 = row * BRICK_HEIGHT + 5
                x2 = x1 + BRICK_WIDTH - 5
                y2 = y1 + BRICK_HEIGHT - 5
                brick = self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue")
                self.bricks.append(brick)

    def move_paddle(self, event):
        paddle_x = event.x
        self.canvas.coords(
            self.paddle,
            paddle_x - PADDLE_WIDTH / 2, WINDOW_HEIGHT - PADDLE_HEIGHT - 10,
            paddle_x + PADDLE_WIDTH / 2, WINDOW_HEIGHT - 10
        )

    def update_game(self):
        # 공 이동
        self.canvas.move(self.ball, self.ball_dx, self.ball_dy)
        ball_coords = self.canvas.coords(self.ball)

        # 벽 충돌
        if ball_coords[0] <= 0 or ball_coords[2] >= WINDOW_WIDTH:
            self.ball_dx = -self.ball_dx
        if ball_coords[1] <= 0:
            self.ball_dy = -self.ball_dy

        # 패들 충돌
        paddle_coords = self.canvas.coords(self.paddle)
        if (ball_coords[2] >= paddle_coords[0] and ball_coords[0] <= paddle_coords[2] and
                ball_coords[3] >= paddle_coords[1] and ball_coords[3] <= paddle_coords[3]):
            self.ball_dy = -self.ball_dy

        # 벽돌 충돌
        for brick in self.bricks:
            brick_coords = self.canvas.coords(brick)
            if (ball_coords[2] >= brick_coords[0] and ball_coords[0] <= brick_coords[2] and
                    ball_coords[3] >= brick_coords[1] and ball_coords[1] <= brick_coords[3]):
                self.canvas.delete(brick)
                self.bricks.remove(brick)
                self.ball_dy = -self.ball_dy
                break

        # 벽돌 내려오기
        for brick in self.bricks:
            self.canvas.move(brick, 0, BRICK_DROP_SPEED)

        # 게임 오버 체크
        if ball_coords[3] >= WINDOW_HEIGHT:
            self.canvas.create_text(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, text="Game Over", fill="white", font=("Arial", 24))
            return

        # 게임 루프
        self.root.after(16, self.update_game)

if __name__ == "__main__":
    root = tk.Tk()
    game = BreakoutGame(root)
    root.mainloop()