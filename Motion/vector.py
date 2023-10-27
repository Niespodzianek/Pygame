import pygame
import random
import time
import math
import os
pygame.init()

PLAYGROUND_SIZE = 900
PLAYGROUND = pygame.display.set_mode((PLAYGROUND_SIZE, PLAYGROUND_SIZE))
pygame.display.set_caption("Gra")
FPS = 60
TOWER_SIZE = 40
RADIUS = 10
SPEED = 1

statek = pygame.transform.scale(pygame.image.load(os.path.join("spaceship_red.png")),(40, 40))
def initial_drawing():
    PLAYGROUND.fill("red")
    pos = [(random.randrange(0 + TOWER_SIZE, PLAYGROUND_SIZE - TOWER_SIZE), random.randrange(0 + TOWER_SIZE, PLAYGROUND_SIZE - TOWER_SIZE)) for _ in range(2)]
    print(pos)
    pygame.draw.rect(PLAYGROUND, "black", (pos[0][0], pos[0][1], TOWER_SIZE, TOWER_SIZE))
    pygame.draw.circle(PLAYGROUND, "blue", (pos[1][0], pos[1][1]), RADIUS)
    pygame.display.update()
    time.sleep(3)
    return pos[0][0], pos[0][1], pos[1][0], pos[1][1]
def drawing(distance, aim_x, aim_y, hunter_x, hunter_y):
    PLAYGROUND.fill("yellow")
    pygame.draw.rect(PLAYGROUND, "black", (aim_x, aim_y, TOWER_SIZE, TOWER_SIZE))
    sinus = (aim_y - hunter_y) / distance
    cosinus = (aim_x - hunter_x) / distance
    print(f"Sinus: {sinus:.4f}, {type(sinus)}, cosinus: {cosinus:.4f}")
    print(math.degrees(math.cos((aim_y - hunter_y) / distance)))
    kat = 180
    PLAYGROUND.blit(pygame.transform.rotate(statek, kat), (hunter_x, hunter_y))
    pygame.display.update()

def tower_move(aim_x, aim_y, hunter_x, hunter_y):
    PLAYGROUND.fill("yellow")
    pygame.draw.rect(PLAYGROUND, "black", (aim_x, aim_y, TOWER_SIZE, TOWER_SIZE))
    pygame.draw.circle(PLAYGROUND, "blue", (hunter_x, hunter_y), RADIUS)
    pygame.display.update()
    return aim_x, aim_y, hunter_x, hunter_y
def distances(aim_x, aim_y, hunter_x, hunter_y):
    result = math.sqrt((hunter_x - aim_x) ** 2 + (hunter_y - aim_y) ** 2)
    print(f"Pozycja łowcy: {hunter_x:.0f}, {hunter_y:.0f} a celu: {aim_x}, {aim_y}, odległość od celu: {result:.4f}")
    return result

def hunter_move(distance, aim_x, aim_y, hunter_x, hunter_y):
    new_hunter_pos_x = (hunter_x - ((hunter_x - aim_x) / distance) * SPEED)
    new_hunter_pos_y = (hunter_y - ((hunter_y - aim_y) / distance) * SPEED)
    return new_hunter_pos_x, new_hunter_pos_y
def main_loop():
    game_speed = pygame.time.Clock()
    game_speed.tick(FPS)
    game_run = True
    start_of_game = True
    aim_x, aim_y, hunter_x, hunter_y = 0, 0, 0, 0
    while game_run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                aim_x, aim_y, hunter_x, hunter_y = (
                    tower_move(aim_x=mouse_position[0], aim_y=mouse_position[1], hunter_x=hunter_x, hunter_y=hunter_y))

        if start_of_game:
            aim_x, aim_y, hunter_x, hunter_y = initial_drawing()
            start_of_game = False

        distance = distances(aim_x, aim_y, hunter_x, hunter_y)
        hunter_x, hunter_y = hunter_move(distance, aim_x, aim_y, hunter_x, hunter_y)
        drawing(distance, aim_x, aim_y, hunter_x, hunter_y)
        time.sleep(2)
    pygame.quit()
def program():
    main_loop()

if __name__ == "__main__":
    program()
    print("KONIEC PRACY PROGRAMU")
