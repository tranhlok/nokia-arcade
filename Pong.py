'''
Nokia Arcade - A project by Lucas Tran
Ping Pong and UI part
December 10, 2018
'''
import pygame
import sys
from pygame.locals import*
from Snake import main as main_1

pygame.init()

fieldimg = pygame.image.load('E:\\College\\Freshman\\First Semester\\CS 111\\Final Project\\field2.jpg')

window_height = 800
window_width = 1000
display_surf = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Nokia Arcade - A Project by Lucas Tran")
fps = 200
fps_clock = pygame.time.Clock()

smallfont = pygame.font.SysFont('comicsansms', 25)
medfont = pygame.font.SysFont('comicsansms', 50)
largefont = pygame.font.SysFont('comicsansms', 80)

GREEN = (72, 150, 32)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (200, 0, 0)
LIGHTRED = (255, 0, 0)
YELLOW = (200, 200, 0)
LIGHTYELLOW = (255, 255, 0)
LIGHTGREEN = (91, 189, 43)

def Button(text, x, y, width, height, inactive_color, active_color, action=None):
    '''
    Get the position from the mouse, check if it in the area of the box button
    and do corresponding line

    text: The text
    x: loaction of the box
    y: location of the box
    width: width of the box
    height: height of the box
    inactive_color: color when inactive
    active_color: color when active (when you point the mouse to it)
    '''
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(display_surf, active_color, (x, y, width, height))
        if click[0] == 1 and action != None:
            if action == 'quit':
                pygame.quit()
                quit()
            if action == 'pong':
                main()
            if action == 'snake':
                main_1()
    else:
        pygame.draw.rect(display_surf, inactive_color, (x, y, width, height))
    Text().text_to_button(text, BLACK, x, y, width, height)

def game_intro():
    '''
    Create the game intro, add the text and color to the buttons

    None
    '''
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_c:
                    intro = False

        Game().text.message_to_screen('Nokia Arcade', WHITE, -100, 'large')


        pygame.draw.rect(display_surf, BLACK, (window_width / 2 - 100, window_height / 2 + 100, 200, 50))
        pygame.draw.rect(display_surf, BLACK, (window_width / 2 - 100, window_height / 2 + 200, 200, 50))
        pygame.draw.rect(display_surf, BLACK, (window_width / 2 - 100, window_height / 2 + 300, 200, 50))

        Text().text_to_button('A Project by Lucas Tran', WHITE, window_width / 2 - 100, window_height / 2, 200, 50, 'medium')
        Button('snake', window_width / 2 - 100, window_height / 2 + 100, 200, 50, WHITE, RED, action='snake')
        Button('ping pong', window_width / 2 - 100, window_height / 2 + 200, 200, 50, WHITE, RED, action='pong')
        Button('mom is watching', window_width / 2 - 100, window_height / 2 + 300, 200, 50, RED, YELLOW, action='quit')

        pygame.display.update()
        fps_clock.tick(15)

class Text:
    def text_objects(self, text, color, size):
        '''
        Modify the text size

        self: objet
        text: the text
        color: the color
        size: font size
        '''
        if size == "small":
            textSurface = smallfont.render(text, True, color)
        elif size == "medium":
            textSurface = medfont.render(text, True, color)
        elif size == "large":
            textSurface = largefont.render(text, True, color)
        return textSurface, textSurface.get_rect()

    def text_to_button(self, msg, color, button_x, button_y, button_width, button_height, size='small'):
        '''
        Add text to button
        '''
        textSurf, textRect = self.text_objects(msg, color, size)
        textRect.center = ((button_x + (button_width / 2)), button_y + (button_height / 2))
        display_surf.blit(textSurf, textRect)

    def message_to_screen(self, msg, color, y_displace=0, size="small"):
        '''
        Show the message on the screen (title of the project)
        '''
        textSurf, textRect = self.text_objects(msg, color, size)
        textRect.center = (window_width / 2), (window_height / 2) + y_displace
        display_surf.blit(textSurf, textRect)

class Paddle:
    def __init__(self, x, w, h):
        '''
        The __init__ method is run as soon as an object of a class
        is instantiated. Its aim is to initialize the object
        '''
        self.w = w
        self.h = h
        self.x = x
        self.y = window_height / 2
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

    def draw(self):
        '''
        Draw the paddle
        '''
        pygame.draw.rect(display_surf, BLACK, self.rect)

    def move(self, pos):
        '''
        Draw the paddle based on their motion
        '''
        self.rect.y = pos[1]
        self.draw()


class AutoPaddle(Paddle):
    def __init__(self, x, w, h, speed, ball):
        '''
        The __init__ method is run as soon as an object of a class
        is instantiated. Its aim is to initialize the object
        '''
        super().__init__(x, w, h)
        self.speed = speed
        self.ball = ball

    def move(self):
        '''
        The code that controls the AI machine, making the computer invincible
        '''
        if self.ball.dir_x == 1:
            if self.rect.y + self.rect.h/2 < self.ball.rect.bottom:
                self.rect.y += self.speed
            if self.rect.y + self.rect.h/2 > self.ball.rect.bottom:
                self.rect.y -= self.speed


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
        Display the score
        '''
        result_srf = self.font.render('Score : %s' % score, True, BLACK)
        result_rect = result_srf.get_rect()
        result_rect.topleft = (window_width - 150, 20)
        display_surf.blit(result_srf, result_rect)


class Ball:
    def __init__(self, x, y, w, h, speed):
        '''
        The __init__ method is run as soon as an object of a class
        is instantiated. Its aim is to initialize the object
        '''
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = speed
        self.dir_x = -1  # left = -1 and right = 1
        self.dir_y = -1   # up = -1 and down = 1
        self.rect = pygame.Rect(x, y, w, h)

    def draw(self):
        '''
        Draw the ball
        '''
        pygame.draw.rect(display_surf, BLACK, self.rect)

    def bounce(self, axis):
        '''
        What happen to the ball when it bounces
        '''
        if axis == 'x':
            self.dir_y *= -1
        if axis == 'y':
            self.dir_x *= -1

    def hit_ceiling(self):
        '''
        What happen to the ball when it hit the ceilling
        '''
        if self.dir_y == -1 and self.rect.top <= self.h:
            return True
        else:
            return False

    def hit_floor(self):
        '''
        What happen to the ball when it hit the floor
        '''
        if self.dir_y == 1 and self.rect.bottom >= window_height - self.h:
            return True
        else:
            return False

    def hit_wall(self):
        '''
        What happen to the ball when it hit the wall
        '''
        if (self.dir_x == -1 and self.rect.left <= self.w) or (self.dir_x == 1 and self.rect.right >= window_width - self.w):
            return True
        else:
            return False

    def hit_paddle_user(self, paddle):
        '''
        What happen to the ball when it hit the paddle of the user
        '''
        if self.rect.left == paddle.rect.right and self.rect.bottom >= paddle.rect.top and self.rect.top <= paddle.rect.bottom:
            return True
        else:
            return False

    def hit_paddle_computer(self, paddle):
        '''
        What happen to the ball when it hit the paddle of the computer
        '''
        if self.rect.right == paddle.rect.left and self.rect.bottom >= paddle.rect.top and self.rect.top <= paddle.rect.bottom:
            return True
        else:
            return False

    def move(self):
        '''
        Control the movement mechanics of the ball
        '''
        self.rect.x += (self.dir_x * self.speed)
        self.rect.y += (self.dir_y * self.speed)
        if self.hit_ceiling() or self.hit_floor():
            self.bounce('x')


class Game:
    def __init__(self, line_thickness=10, speed=2):
        '''
        The __init__ method is run as soon as an object of a class
        is instantiated. Its aim is to initialize the object
        '''
        self.line_thickness = line_thickness
        self.speed = speed
        ball_x = window_width / 2
        ball_y = window_height / 2
        ball_w = self.line_thickness
        ball_h = self.line_thickness
        self.ball = Ball(ball_x, ball_y, ball_w, ball_h, self.speed)
        self.paddles = {}
        paddle_x = 20
        paddle_w = self.line_thickness
        paddle_h = 50
        self.paddles['user'] = Paddle(paddle_x, paddle_w, paddle_h)
        self.paddles['computer'] = AutoPaddle(window_width - paddle_x - 10, paddle_w, paddle_h, self.speed, self.ball)
        self.score = ScoreBoard()
        self.text = Text()

    def draw_arena(self):
        '''
        Draw and add image into the background
        '''
        display_surf.blit(fieldimg, (0, 0))

    def update(self):
        '''
        Update the score by calling previous function related to ball movement
        '''
        self.draw_arena()
        self.ball.draw()
        self.paddles['user'].draw()
        self.paddles['computer'].draw()
        self.ball.move()
        self.paddles['computer'].move()
        if self.ball.hit_paddle_user(self.paddles['user']):
            self.ball.bounce('y')
            self.score.score += 1
        self.score.display(self.score.score)
        if self.ball.hit_paddle_computer(self.paddles['computer']):
            self.ball.bounce('y')


def main():
    pygame.init()
    game = Game()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEMOTION:
                game.paddles['user'].move(event.pos)
        game.update()
        if game.ball.hit_wall():
            break
        pygame.display.update()
        fps_clock.tick(fps)
    print('Your Ping Pong Game Score:', game.score.score)

if __name__ == '__main__':
    game_intro()
    main()
