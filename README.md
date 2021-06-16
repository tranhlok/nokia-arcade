# nokia-arcade
CS111 Final Project
This is an old copy of my intro to CS project from 2018 

I/ Title 

- Title of the project: Nokia Arcade
- Name: Tran Anh Loc
- Date: December 10, 2018

II/ Introduction 

- Purpose: I want to do something fun with my final project.
- Background: For this final project, I will do something different from what we have done
in class. I’m not fascinated with data, graph or any kind of science – biology, chemistry,
physics – related models and numbers, but I really like to play games and want to learn
how to make one for myself. So I looking for some article about how to make game with
python (the program language that we have learnt about in this intro class) and I found
a library called pygame that can helps me create some simple old-school 90s like games.
I want to create something common, something that recalls the childhood memories
about games of everybody. I started to think about what game I play the most back in
that time and I immediately think about my dad’s old Nokia cellphone that has all the
coolest game at that time, including Snake and Ping Pong.

- The problem is interesting because it is exactly what I wanted to do in the future: A
game designer. 

III/ Methods 

1/ Overview 

The first game will be the ping pong game, where user will fight against computer in a
paddle-hit-ball type of match. I will have to create code to automatically run the paddle
to hit the ball. The computer will not lose in any situation, in other word, the computer
will be invincible in this game. There will be only one goal for the player: Have the
highest score possible, each time the ball hit the paddle will result in one-point count to
the user. The game will end when the ball touches the wall behind the player’s paddle.
This game will use mouse motion to control the paddle, as you can react faster with the
change in direction of the ball.

The second game will be the snake game, you already know what it is right! In this
game, player will also have one single task: Score as highest point as possible. Player will
also have to avoid crash their snake into wall or to the snake’s body. The game will end
if one of those possibility happens. This game will use keyboard arrow keys to control
the snake, as I want the recreate the control system on the old Nokia phones.

2/ My Algorithm

(a) The Ping Pong Game

This game builds up from two different modules: pygame and sys.
This game has 6 class: Text, Paddle, AutoPaddle, ScoreBoard, Ball, Game.
The code start by import pygame and sys module, copy all names in pygame.locals
into your current namespace (saves you typing), and import the main class of the
second game. The it runs the line pygame.init() to launch pygame module. Then it
creates some global variables:

- fieldimg: the background image of the game (in this case it’s Dr. White’s face).
- window_height: The height of the window.
- window_width: the width of the window.
- display_surf: The display surface created by pygame module.
- Set caption for the window.
- fps and fps_clock: This method should be called once per frame. It will compute
how many milliseconds have passed since the previous call.
- smallfont, medfont and largefont: Some fonts that the program will need to create
the UI.
- GREEN, BLACK, WHITE, RED, LIGHTRED, YELLOW, LIGHTYELLOW, LIGHTGREEN: The
colors tuples that I created based on the RGB table. The program will use these
colors as inputs. The reason I created many colors tuples that I don’t use is it’s easier
for u to play with my program (In case you want to do that).
After creates all these variables, I create two outside the class functions: Button and
game_intro. The first function, Button, takes 8 parameters: text, x, y, width, height,
inactive_color, active_color, action=None. First it gets the position of the mouse and
click motion from the user and stores those values in two variables. If the mouse
goes into the area of the box, it will the change the color of the box to different
colors. An if you click in one of these box, it will run the corresponded function to
that box or quit the game. If the mouse is not in the area of the box, it will show a box with original color. Then it adds text to the button by calling the function
text_to_button inside the class Text. The next function, game_intro, takes no
parameter. This function basically creates a text box and the title of the game, then
it calls the previous Button function to add texts and the reflective effects to these
box buttons.
The next thing I’m going to talk about are classes, I will not talk about the __init__
function in every class because its aim is just to initialize the object. Nothing much to
talk about here.
The first class is Text, a class created to modify the text mainly in the creation of the
UI, contains 3 functions: text_objects, text_to_button, message_to_screen. The
function text_objects sets the size of the text and renders it to the screen. This
function return the text. The function text_to_button add the text return by the
previous function and draw it on the location of the color box. The last function in
this class, message_to_screen, shows the text to screen (in this case the title of the
project). This function has no return value.
The second class is Paddle, this class contains 3 functios: __init__, draw and move.
The draw takes self (the object) as its only parameter. This function draws the
paddle by using the function draw from the pygame module. The next function,
move, simply moves the paddle by taking self and position as parameters. This
function has no return value.
The AutoPaddle class has two function: __init__, move. The move function takes
self (the object) as its single parameter. This function uses a range of if statements
to control the auto paddle along with the position of the ball, making computer’s
paddle invincible. This function has no return value.
The ScoreBoard class has two functions: __init__ and display. The display function
simply displays the score of the user by some built-in function like render, get_rect
and blit.
The Ball class has 9 functions: __init__, draw, bounce, hit_ceiling, hit_floor,
hit_wall, hit_paddle_user, hit_paddle_computer, move. The function draw takes
one parameter: self, then it draws the ball by function draw.rect in pygame module.
This function has no return value. The function bounce takes two parameters: self
and axis. In this function, the machine starts a Boolean to change the direction of
the ball in some circumstances. This function has no return value. The function
hit_ceiling only has 1 parameter: self. This function compares the dimension of the
ball with the height of the window to check if it hit the ceiling or not. This function
returns True when the ball hit the ceiling and false if it not. The function hit_floor
only has 1 parameter: self. This function compares the dimension of the ball with the
height of the window to check if it hit the floor or not. This function returns True
when the ball hit the floor and false if it’s not. The function hit_wall only has 1
parameter: self. This function compares the dimension of the ball with the height of
the window to check if it hit the wall or not. This function returns True when the ball
hit the wall and false if it not. The function hit_paddle_user only has 2 parameters:
self and paddle. This function compares the dimension of the ball with the height of
the window and paddle to check if it hit the user’s paddle or not. This function
returns True when the ball hit the user’s paddle and false if it not. The function hit_
paddle_computer only has 2 parameters: self and paddle. This function compares
the dimension of the ball with the height of the window and the paddle to check if it
hit the computer’s paddle or not. This function returns True when the ball hit the
computer’s paddle and false if it not. The last function move controls the movement
mechanics of the ball. It will bounce the ball if it touches the ceiling or floor. This
function has no return value.
The class Game has three functions: __init__, draw_arena, update. The draw_arena
function simply draws the area of the game and fills it with Dr. White’s face. This
function has no return value. The update function updates the score by calling
previous function related to ball movement. It also draws the arena, the two paddles
and the ball. If the ball hit the user’s paddle, the score will increase one. If the ball
hit the opponent’s paddle, the ball will bounce by a different angle. This function has
no return value.
The main function simply calls all the function above and print out the score of user
at the end of the game. It also has the code for the movement (how the computer
transforms mouse motions into directions)

(b) The Snake Game 
This game builds up from three different modules: pygame, random and time.
This game has 6 class: Food, Snake, Game, ScoreBoard
The code start by import pygame, random and time module, copy all names in
pygame.locals into your current namespace (saves you typing), and import the main
class of the second game. The it runs the line pygame.init() to launch pygame
module. Then it creates some global variables:
- fieldimg: the background image of the game (in this case it’s Dr. White’s face).
- window_height: The height of the window.
- window_width: the width of the window.
- display_surf: The display surface created by pygame module.
- Set caption for the window.
- fps and fps_clock: This method should be called once per frame. It will compute
how many milliseconds have passed since the previous call.
- smallfont, medfont and largefont: Some fonts that the program will need to create
the UI.
- GREEN, BLACK, WHITE, RED, LIGHTRED, YELLOW, LIGHTYELLOW, LIGHTGREEN: The
colors tuples that I created based on the RGB table. The program will use these
colors as inputs. The reason I created many colors tuples that I don’t use is it’s easier
for u to play with my program (In case you want to do that).
The next thing I’m going to talk about are classes, I will not talk about the __init__
function in every class because its aim is just to initialize the object. Nothing much to
talk about here.
The Food class has two function: __init__ and generate. The generate function
creates a food on the surface of the display by using a function called draw.rect in
the pygame module. This function has no return value.
The Snake class has 9 functions: __init__, draw, grow, hit_ceiling, hit_floor,
hit_wall, move. The function draw takes one parameter: self, then it draws the
snake by function draw.rect in pygame module. This function has no return value.
The function grow takes one parameter: self. In this function, the machine grows the
snake by one for everytime it touches the food. This function has no return value.
The function hit_ceiling only has 1 parameter: self. This function compares the
location of the snake with the height of the window to check if it hit the ceiling or
not. This function returns True when the snake hit the ceiling and false if it not. The
function hit_floor only has 1 parameter: self. This function compares compares the
location of the snake with the height of the window to check if it hit the floor or not.
This function returns True when the ball hit the floor and false if it’s not. The
function hit_wall only has 1 parameter: self. This function compares compares the
location of the snake with the height of the window to check if it hit the wall or not.
This function returns True when the ball hit the wall and false if it not. The last
function move controls the movement mechanics of the ball. It will bounce the ball
if it touches the ceiling or floor. This function has no return value.
The ScoreBoard class has two functions: __init__ and display. The display function
simply displays the score of the user by some built-in function like render, get_rect
and blit.
The Game class contains four functions: __init__, collision, draw_arena and update.
The collision function returns True when the snake hit the something (from the
input), and False otherwise. This function has no return value. The draw_arena
function simply fills the space with an image of famous singer Justin Bieber. This
function has no return value. The update function firstly draws the arena, generates
the food. Then it checks if the snake hit the wall, floor or ceiling or not. Then it starts
a for loop that iterates through each part of the snake to check if the snake hit itself.
Then it creates another if statement in case the snake hit the food. In this case, the
machine will generate a new location of the food by the random function, grow a
snake by 1 and add 1 to the score. This function has no return value.
The main function is where the whole game started. It also has the code for the
movement (how the computer transforms keys into directions).
