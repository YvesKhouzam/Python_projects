import pygame
from pygame.locals import *
import time
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 1000
SIZE = 40


class Apple:
    def __init__(self, parent_screen):
        self.apple = pygame.image.load('resources/apple.jpg').convert()
        self.parent_screen = parent_screen
        self.x = SIZE*3
        self.y = SIZE*3

    def draw(self):
        self.parent_screen.blit(self.apple, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(0, int(SCREEN_WIDTH/SIZE))*SIZE
        self.y = random.randint(0, int(SCREEN_HEIGHT/SIZE))*SIZE


class Snake:
    def __init__(self, parent_screen, length):
        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x = [SIZE]*length
        self.y = [SIZE]*length
        self.direction = 'down'

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def draw(self):
        self.parent_screen.fill((110, 110, 5))
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

    def move_left(self):
        self.direction = 'left'
        self.draw()

    def move_right(self):
        self.direction = 'right'
        self.draw()

    def move_up(self):
        self.direction = 'up'
        self.draw()

    def move_down(self):
        self.direction = 'down'
        self.draw()

    def walk(self):

        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'left':
            self.x[0] -= SIZE
        self.draw()


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.fill((110, 110, 5))
        self.snake = Snake(self.surface, 1)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def is_collision(self, x1, y1, x2, y2):
        if x2 <= x1 < x2 + SIZE:
            if y2 <= y1 < y2 + SIZE:
                return True
        return False

    def play(self):
        self.snake.walk()
        self.apple.draw()

        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.apple.move()
            self.snake.increase_length()

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_UP:
                        self.snake.move_up()
                    if event.key == K_DOWN:
                        self.snake.move_down()
                    if event.key == K_LEFT:
                        self.snake.move_left()
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                elif event.type == QUIT:
                    running = False

            self.play()

            time.sleep(0.2)

    def fill(self, param):
        pass


if __name__ == "__main__":
    game = Game()
    game.run()

    pygame.display.flip()




