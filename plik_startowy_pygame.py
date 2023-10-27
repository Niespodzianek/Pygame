import pygame
pygame.init()

WYSOKOSC_PLANSZY, SZEROKOSC_PLANSZY = 1000, 1000
PLANSZA_GRY = pygame.display.set_mode((SZEROKOSC_PLANSZY, WYSOKOSC_PLANSZY))
pygame.display.set_caption("Gra")
FPS = 60

def drawing(gracz):
    PLANSZA_GRY.fill("red")
    pygame.draw.rect(PLANSZA_GRY, "white", (gracz.x, gracz.y, gracz.width, gracz.height))
    pygame.display.update()

def main_loop():
    game_speed = pygame.time.Clock()
    game_speed.tick(FPS)

    gracz = pygame.Rect(500, 500, 200, 200)
    print(type(gracz))
    print(dir(gracz))
    input("Naciśnij ENTER")

    program_pracuje = True
    while program_pracuje:
        for zdarzenie in pygame.event.get():
            if zdarzenie.type == pygame.QUIT:
                program_pracuje = False

        drawing(gracz)
    pygame.quit()

def program():
    main_loop()

if __name__ == "__main__":
    program()
    print("KONIEC PRACY PROGRAMU")
