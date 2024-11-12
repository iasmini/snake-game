import random
from PIL import Image, ImageTk
from tkinter import Tk, Frame, Canvas, ALL, NW

WIDTH = 300
HEIGHT = 300
DOT_SIZE = 10
DELAY = 100
RAND_POS = 27


class Snake(Frame):
    def __init__(self):
        super().__init__()
        self.master.title('Snake Game')
        self.board = Canvas(self, width=WIDTH, height=HEIGHT, background='black')
        self.pack()
        self.board.pack()
        self.load_images()
        self.init_game()
        self.bind_all("<KeyPress>", self.on_key_pressed)
        self.after(DELAY, self.on_timer)

    def load_images(self):
        """Carrega as imagens da cabeça e do corpo da cobra."""
        self.dot_image = ImageTk.PhotoImage(Image.open("dot.png"))
        self.head_image = ImageTk.PhotoImage(Image.open("head.png"))

    def init_game(self):
        """Inicializa o estado do jogo."""
        self.in_game = True
        self.score = 0

        # Posição inicial da cobra e maçã
        self.snake = [(50, 50), (40, 50), (30, 50)]
        self.apple = self.place_apple()

        self.direction = 'Right'
        self.draw_objects()

    def place_apple(self):
        """Coloca a maçã em uma posição aleatória."""
        x = random.randint(0, RAND_POS) * DOT_SIZE
        y = random.randint(0, RAND_POS) * DOT_SIZE
        return (x, y)

    def draw_objects(self):
        """Desenha a cobra e a maçã na tela."""
        self.board.delete(ALL)

        # Desenha a maçã
        x, y = self.apple
        self.board.create_image(x, y, image=self.dot_image, anchor=NW)

        # Desenha a cobra
        for i, (x, y) in enumerate(self.snake):
            image = self.head_image if i == 0 else self.dot_image
            self.board.create_image(x, y, image=image, anchor=NW)

    def check_collisions(self):
        """Verifica se houve colisões com as bordas ou consigo mesma."""
        x, y = self.snake[0]
        if (x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT or
                (x, y) in self.snake[1:]):
            self.in_game = False

    def move_snake(self):
        """Move a cobra para a próxima posição."""
        x, y = self.snake[0]

        # Ajusta a posição para atravessar as bordas
        if self.direction == 'Left':
            x = (x - DOT_SIZE) % WIDTH
        elif self.direction == 'Right':
            x = (x + DOT_SIZE) % WIDTH
        elif self.direction == 'Up':
            y = (y - DOT_SIZE) % HEIGHT
        elif self.direction == 'Down':
            y = (y + DOT_SIZE) % HEIGHT

        # Insere a nova posição no início da lista
        self.snake.insert(0, (x, y))

        # Verifica se a cobra comeu a maçã
        if (x, y) == self.apple:
            self.apple = self.place_apple()
            self.score += 1
        else:
            # Remove a última parte da cobra
            self.snake.pop()

    def on_key_pressed(self, event):
        """Muda a direção da cobra com base na tecla pressionada."""
        key = event.keysym
        directions = {'Left', 'Right', 'Up', 'Down'}
        if key in directions:
            # Impede a cobra de ir na direção oposta imediatamente
            opposite = {'Left': 'Right', 'Right': 'Left',
                        'Up': 'Down', 'Down': 'Up'}
            if key != opposite.get(self.direction):
                self.direction = key

    def on_timer(self):
        """Controla o loop do jogo."""
        if self.in_game:
            self.check_collisions()
            self.move_snake()
            self.draw_objects()
            self.after(DELAY, self.on_timer)
        else:
            self.game_over()

    def game_over(self):
        """Exibe a mensagem de fim de jogo."""
        self.board.delete(ALL)
        self.board.create_text(WIDTH / 2, HEIGHT / 2,
                               text=f"Game Over! Score: {self.score}",
                               fill='white', font=('Arial', 20))


def main():
    root = Tk()
    Snake()
    root.mainloop()


if __name__ == '__main__':
    main()
