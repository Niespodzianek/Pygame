import pygame
import os

WYSOKOSC_PLANSZY, SZEROKOSC_PLANSZY = 500, 900
PLANSZA_GRY = pygame.display.set_mode((SZEROKOSC_PLANSZY, WYSOKOSC_PLANSZY))
pygame.display.set_caption("Gra")

FPS = 60

sciezka_do_pliku_zoltego_statku = os.path.join("spaceship_yellow.png")
GRAFIKA_STATEK_ZOLTY = pygame.image.load(sciezka_do_pliku_zoltego_statku)
WYSOKOSC_STATKU, SZEROKOSC_STATKU = 50, 50
STATEK_ZOLTY = pygame.transform.rotate(pygame.transform.scapiple(GRAFIKA_STATEK_ZOLTY,
                                                              (SZEROKOSC_STATKU, WYSOKOSC_STATKU)), 90)

def etap_rysowania_gry(zolty_gracz):
    PLANSZA_GRY.fill("red")
    PLANSZA_GRY.blit(STATEK_ZOLTY, (zolty_gracz.x, zolty_gracz.y))
    pygame.display.update()

def sterowanie_graczem(a, v, t, wcisniety_klawisz, zolty_gracz):
    if wcisniety_klawisz[pygame.K_d]:                                                 # ruch jednostajnie przyśpieszony
        a = a * 1.005
        v = a * t
    s = v * t
    zolty_gracz.x += s
    print(f"Prędkość gracza: {v}, przyśpieszenie gracza: {a}")
    return a, v, s

def logika_gry(tempo_gry, FPS):
    a = 2
    t = 1
    v = a * t
    droga = 0
    zolty_gracz = pygame.Rect(0, 300, SZEROKOSC_STATKU, WYSOKOSC_STATKU)
    
    tempo_gry.tick(FPS)
    program_pracuje = True
    while program_pracuje:
        for zdarzenie in pygame.event.get():
            if zdarzenie.type == pygame.QUIT:
                program_pracuje = False

        wcisniety_klawisz = pygame.key.get_pressed()

        a, v, s = sterowanie_graczem(a, v, t, wcisniety_klawisz, zolty_gracz)
        droga += s
        print(f"Przebyto: {droga}")

        etap_rysowania_gry(zolty_gracz)
    pygame.quit()

def gra():
    tempo_gry = pygame.time.Clock()
    logika_gry(tempo_gry, FPS)

if __name__ == "__main__":
    gra()
    print("KONIEC PRACY PROGRAMU")
