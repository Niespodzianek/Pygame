import pygame
import os

WYSOKOSC_PLANSZY, SZEROKOSC_PLANSZY = 500, 900
PLANSZA_GRY = pygame.display.set_mode((SZEROKOSC_PLANSZY, WYSOKOSC_PLANSZY))
pygame.display.set_caption("Gra")

FPS = 60

sciezka_do_pliku_zoltego_statku = os.path.join("../Statki/Grafika", "spaceship_yellow.png")
sciezka_do_pliku_czerwonego_statku = os.path.join("../Statki/Grafika", "spaceship_red.png")

GRAFIKA_STATEK_ZOLTY = pygame.image.load(sciezka_do_pliku_zoltego_statku)
GRAFIKA_STATEK_CZERWONY = pygame.image.load(sciezka_do_pliku_czerwonego_statku)

WYSOKOSC_STATKU, SZEROKOSC_STATKU = 100, 100

STATEK_ZOLTY = pygame.transform.rotate(pygame.transform.scale(GRAFIKA_STATEK_ZOLTY, (SZEROKOSC_STATKU, WYSOKOSC_STATKU)), 90)
STATEK_CZERWONY = pygame.transform.rotate(pygame.transform.scale(GRAFIKA_STATEK_CZERWONY, (SZEROKOSC_STATKU, WYSOKOSC_STATKU)), 270)

SZYBKOSC = 2

def etap_rysowania_gry(zolty_gracz, czerwony_gracz):
    PLANSZA_GRY.fill("red")
    PLANSZA_GRY.blit(STATEK_ZOLTY, (zolty_gracz.x, zolty_gracz.y))
    PLANSZA_GRY.blit(STATEK_CZERWONY, (czerwony_gracz.x, czerwony_gracz.y))
    pygame.display.update()

def logika_gry(tempo_gry, FPS):
    zolty_gracz = pygame.Rect(100, 300, SZEROKOSC_STATKU, WYSOKOSC_STATKU)
    czerwony_gracz = pygame.Rect(700, 300, SZEROKOSC_STATKU, WYSOKOSC_STATKU)

    tempo_gry.tick(FPS)
    program_pracuje = True
    while program_pracuje:
        for zdarzenie in pygame.event.get():
            if zdarzenie.type == pygame.QUIT:
                program_pracuje = False

        wcisniety_klawisz = pygame.key.get_pressed()
        if wcisniety_klawisz[pygame.K_a]:
            zolty_gracz.x -= SZYBKOSC
            if zolty_gracz.x < 0:
                zolty_gracz.x = 0
        if wcisniety_klawisz[pygame.K_s]:
            zolty_gracz.x += SZYBKOSC
            if zolty_gracz.x > SZEROKOSC_PLANSZY - SZEROKOSC_STATKU:
                zolty_gracz.x = SZEROKOSC_PLANSZY - SZEROKOSC_STATKU

        etap_rysowania_gry(zolty_gracz, czerwony_gracz)
    pygame.quit()

def gra():
    tempo_gry = pygame.time.Clock()
    logika_gry(tempo_gry, FPS)

if __name__ == "__main__":
    gra()
    print("KONIEC PRACY PROGRAMU")
