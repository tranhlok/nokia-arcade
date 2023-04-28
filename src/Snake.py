'''
Nokia Arcade - A project by Lucas Tran
Snake Part
December 10, 2018
I don't think this is going to run due to package difference, but it's a good memory 4sure
'''
import pygame
import random
from time import sleep
from pygame.locals import*

fieldimg = pygame.image.load('../resources/field.jpg')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (72, 150, 32)
RED = (200, 0, 0)
LIGHTRED = (255, 0, 0)
YELLOW = (200, 200, 0)
LIGHTYELLOW = (255, 255, 0)
LIGHTGREEN = (91, 189, 43)

window_height = 800
window_width = 1000
display_surf = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake")
fps = 20
fps_clock = pygame.time.Clock()


class Food:
    def __init__(self, x, y):
        '''
        The __init__ method is run as soon as an object of a class
        is instantiated. Its aim is to initialize the object
        '''
        self.x = x
        self.y = y

    def generate(self):
        '''
        Create the food on the screen surface
        '''
        pygame.draw.rect(display_surf, RED, pygame.Rect(self.x, self.y, 10, 10))


class Snake:
    def __init__(self, x, y, food_pos):
        '''
        The __init__ method is run as soon as an object of a class
        is instantiated. Its aim is to initialize the object
        '''
        self.g = 0
        self.food_pos = food_pos
        self.x = 60
        self.y = 40
        self.cells = [(x - 20, y), (x - 10, y), (x, y)]
        self.dir_x = 1
        self.dir_y = 0

    def move(self):
        '''
        movement mechanics of the snake
        '''
        del self.cells[0]
        self.cells.append((self.cells[-1][0]+self.dir_x*10, self.cells[-1][1]+self.dir_y*10))

    def draw(self):
        '''
        Draw the snake
        '''
        for i in self.cells:
            pygame.draw.rect(display_surf, WHITE, pygame.Rect(int(i[0]+1), int(i[1]+1), 8, 8))

    def grow(self):
        '''
        Grow the snake by one everytime it touches the food
        '''
        self.cells.insert(0, self.cells[0])

    def hit_ceiling(self):
        '''
        What happen to the snake when it hit the ceilling
        '''
        if self.cells[-1][1] <= 0:
            return True
        else:
            return False

    def hit_floor(self):
        '''
        What happen to the snake when it hit the floor
        '''
        if self.cells[-1][1]+10 >= window_height:
            return True
        else:
            return False

    def hit_wall(self):
        '''
        What happen to the snake when it hit the wall
        '''
        if self.cells[-1][0] <= 0 or self.cells[-1][0]+10 >= window_width:
            return True
        else:
            return False


class ScoreBoard:
    def __init__(self, font_size=20, score=0):
        '''
        The __init__ method is run as soon as an object of a class
        is instantiated. Its aim is to initialize the object
        '''
        self.x = window_width - 150
        self.y = 20
        self.score = score
        self.font = pygame.font.SysFont('comicsansms', font_size)

    def display(self, score):
        '''
        Display the score broad to screen surface
        '''
        result_srf = self.font.render('Score : %s' % score, True, BLACK)
        result_rect = result_srf.get_rect()
        result_rect.topleft = (window_width - 150, 20)
        display_surf.blit(result_srf, result_rect)


class Game:
    def __init__(self):
        '''
        The __init__ method is run as soon as an object of a class
        is instantiated. Its aim is to initialize the object
        '''
        self.q = 0
        snake_x = window_width / 2
        snake_y = window_height / 2
        x = 10 * random.randint(1, 38)
        y = 10 * random.randint(1, 28)
        self.food = Food(x, y)
        self.food.generate()
        self.snake = Snake(snake_x, snake_y, (self.food.x, self.food.y))
        self.score = ScoreBoard()

    @staticmethod
    def collision(x1, y1, x2, y2):
        '''
        When the sanke hits itself or hit the food
        '''
        if x2 < x1 < x2 + 10:
            if y2 < y1 < y2 + 10:
                return True
        else:
            return False

    @staticmethod
    def draw_arena():
        '''
        Draw the arena and add the background to it
        '''
        display_surf.blit(fieldimg, (0, 0))

    def update(self):
        '''
        Update all the actions that happen inside the game
        '''
        self.draw_arena()
        self.food.generate()
        self.snake.food_pos = (self.food.x, self.food.y)
        self.snake.move()
        self.snake.draw()
        if self.snake.hit_wall() or self.snake.hit_floor() or self.snake.hit_ceiling():
            self.q = 1
        for i in range(len(self.snake.cells) - 1):
            if self.collision(self.snake.cells[-1][0]+5, self.snake.cells[-1][1]+5, self.snake.cells[i][0], self.snake.cells[i][1]):
                self.q = 1
                break
        if self.collision(self.snake.cells[-1][0]+5, self.snake.cells[-1][1]+5, self.food.x, self.food.y):
            x = 10 * random.randint(1, 78)
            y = 10 * random.randint(1, 58)
            self.food = Food(x, y)
            self.snake.grow()
            self.food.generate()
            self.score.score += 1
        self.score.display(self.score.score)


def main():
    pygame.init()
    game = Game()
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == 273 and not game.snake.dir_y == 1:
                        game.snake.dir_y = -1
                        game.snake.dir_x = 0
                elif event.key == 274 and not game.snake.dir_y == -1:
                        game.snake.dir_y = 1
                        game.snake.dir_x = 0
                elif event.key == 276 and not game.snake.dir_x == 1:
                        game.snake.dir_y = 0
                        game.snake.dir_x = -1
                elif event.key == 275 and not game.snake.dir_x == -1:
                        game.snake.dir_y = 0
                        game.snake.dir_x = 1
        game.update()
        if game.q == 1:
            sleep(1.3)
            break
        pygame.display.update()
        fps_clock.tick(fps)
    print('Your Snake Game Score:', game.score.score)


if __name__ == '__main__':
    main()
