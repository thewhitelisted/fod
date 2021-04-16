# imports
import os
import sys
import random

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

# initialize pygame
pygame.init()

# initialize the screen
size = width, height = 1000, 1000
a = pygame.image.load('57973c33456641b1d3528522975b29a1.png')
pygame.display.set_icon(a)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("fod")

# color init variables
BLACK = (0, 0, 0)
GREY = (150, 150, 150)
WHITE = (255, 255, 255)
RED = (150, 10, 10)
BLUE = (15, 15, 150)

# player global variables, and rock list
player_x = 50
player_y = 50
y_speed = 0
x_speed = 0
level = 0
end_game = False
rocks = []
player = (player_x, player_y, 50, 50)
foods = []

# text variables
font = pygame.font.SysFont('couriernew', 20)
text = font.render(str(level), True, WHITE)
text_rect = text.get_rect()
text_rect.center = (width // 2, height // 2)


# rock class, contains draw and x, y, w, h, and rect rock (tuple)
class Rock:
    rock = None

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw(self):
        self.rock = pygame.draw.rect(screen, WHITE, (self.x, self.y, self.w, self.h))


class Food:
    food = None

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw(self):
        self.food = pygame.draw.rect(screen, BLUE, (self.x, self.y, self.w, self.h))


def collision(obj) -> bool:
    """
    :param obj:
    :return: bool
    """
    for i in range(50):
        if obj.x + obj.w > player_x + i > obj.x and obj.y < player_y + i < obj.y + obj.h:
            return True
    return False


# draw function, created for the sake of organization. Includes player and rocks
def draw():
    # drawing the background
    screen.fill(BLACK)
    # drawing all rocks based on level
    for i in range(level):
        rocks[i].draw()
    foods[level-1].draw()
    # drawing the actual player
    pygame.draw.rect(screen, GREY, player)
    text = font.render(str(level), True, WHITE)
    screen.blit(text, text_rect)
    # update screen
    pygame.display.flip()


def new_level():
    global level, rocks
    level += 1
    rocks = []
    # for each level, generate a new rock
    for i in range(level):
        rocks.append(Rock(random.randint(10, width - 10), random.randint(10, height - 10), 10, 10))
    foods.append(Food(random.randint(50, width - 50), random.randint(50, height - 50), 10, 10))


# main function
def main():
    # initialize global variables
    global player_x, y_speed, player_y, x_speed, level, player, end_game, food
    new_level()
    while True:
        '''
        gets events from the screen
            if clicked the x on the window, exit app
            if clicked a key on the keyboard
                check if key is wasd
                    affect the player movement accordingly
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    y_speed = -1
                    x_speed = 0
                elif event.key == pygame.K_a:
                    x_speed = -1
                    y_speed = 0
                elif event.key == pygame.K_s:
                    y_speed = 1
                    x_speed = 0
                elif event.key == pygame.K_d:
                    x_speed = 1
                    y_speed = 0

        '''
        adding the x speed and y speed to the x and y of the player
        checking if the player is off the screen, and if so, moves player to the other end of screen
        '''
        player_x += x_speed
        player_y += y_speed
        if player_x + 50 > width:
            player_x = 0
        elif player_y + 50 > height:
            player_y = 0
        elif player_x < 0:
            player_x = width - 50
        elif player_y < 0:
            player_y = height - 50

        player = (player_x, player_y, 50, 50)
        # collision detection for the rocks
        for j in range(len(rocks)):
            if collision(rocks[j]):
                end_game = True
                break

        if collision(foods[level-1]):
            new_level()

        if end_game:
            break

        # refer to draw loop
        draw()


# just initializes main loop
if __name__ == '__main__':
    main()
