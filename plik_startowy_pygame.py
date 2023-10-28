import pygame
pygame.init()

WYSOKOSC_PLANSZY, SZEROKOSC_PLANSZY = 1000, 1000
PLANSZA_GRY = pygame.display.set_mode((SZEROKOSC_PLANSZY, WYSOKOSC_PLANSZY))
pygame.display.set_caption("Gra")
FPS = 60

def drawing():
    PLANSZA_GRY.fill("red")
    pygame.display.update()

def main_loop():
    game_speed = pygame.time.Clock()
    game_speed.tick(FPS)
    program_pracuje = True
    while program_pracuje:
        for zdarzenie in pygame.event.get():
            if zdarzenie.type == pygame.QUIT:
                program_pracuje = False
        drawing()
    pygame.quit()

def program():
    main_loop()

if __name__ == "__main__":
    program()
    print("KONIEC PRACY PROGRAMU")
