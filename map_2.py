WIDTH = 1000
HEGIHT = 500
print()

def map_2(pl1, pl11, pl2, pl22):
    import pygame
    from math import cos, sin, radians
    from classes import Player1, Projectile, Border, Player2

    horizontal_borders = pygame.sprite.Group()
    vertical_borders = pygame.sprite.Group()
    bullets1 = pygame.sprite.Group()
    bullets2 = pygame.sprite.Group()

    amon = pygame.sprite.Sprite()
    gus = pygame.sprite.Sprite()

    p1 = pygame.sprite.Group()
    p2 = pygame.sprite.Group()
    sprites = pygame.sprite.Group()
    amon, gus = Player1(borders_v=vertical_borders, borders_h=horizontal_borders, x=HEGIHT * 0.16, y=HEGIHT * 0.5,
                        type1=pl1, type2=pl11,
                        mybuls=bullets1, others=bullets2, enemy=gus), \
                Player2(borders_v=vertical_borders, borders_h=horizontal_borders,
                        x=WIDTH * 0.93, y=HEGIHT * 0.5, type1=pl2, type2=pl22, mybuls=bullets2,
                        others=bullets1, enemy=amon)
    amon.enemy = gus
    gus.enemy = amon
    sprites.add(amon, gus)
    p1 = pygame.sprite.Group(gus)
    p2 = pygame.sprite.Group(amon)
    gus.add_enemy(p2)
    amon.add_enemy(p1)

    def birth():
        Border(WIDTH * 0.47, HEGIHT * 0.1, WIDTH * 0.53, HEGIHT * 0.1, 'BLACK', sprites, vertical_borders,
               horizontal_borders)  # ГОРМЗОНТ
        Border(WIDTH * 0.485, HEGIHT * 0.07, WIDTH * 0.485, HEGIHT * 0.3, 'BLACK', sprites, vertical_borders,
               horizontal_borders)  # ВЕРТИАЛ
        Border(WIDTH * 0.3, HEGIHT * 0.55, WIDTH * 0.4, HEGIHT * 0.55, 'BLACK', sprites, vertical_borders,
               horizontal_borders)  # ГОРИЗОНТ

        Border(WIDTH * 0.35, HEGIHT * 0.41, WIDTH * 0.35, HEGIHT * 0.61, 'BLACK', sprites, vertical_borders,
               horizontal_borders)  # ВЕРТИКАЛЬ
        Border(WIDTH * 0.6, HEGIHT * 0.3, WIDTH * 0.75, HEGIHT * 0.3, 'BLACK', sprites, vertical_borders,
               horizontal_borders)  # ГОРИЗОНТ

        Border(WIDTH * 0.55, HEGIHT * 0.4, WIDTH * 0.55, HEGIHT * 0.7, 'BLACK', sprites, vertical_borders,
               horizontal_borders)  # ВЕРТИКАЛЬ

        Border(WIDTH * 0.18, HEGIHT * 0.8, WIDTH * 0.4, HEGIHT * 0.8, 'BLACK', sprites, vertical_borders,
               horizontal_borders)  # ГОРИЗОНТ

        Border(WIDTH * 0.05, HEGIHT * 0.32, WIDTH * 0.13, HEGIHT * 0.32, 'BLACK', sprites, vertical_borders,
               horizontal_borders)  # ГОРИЗОНТ

        Border(WIDTH * 0.05, HEGIHT * 0.179, WIDTH * 0.05, HEGIHT * 0.32, 'BLACK', sprites, vertical_borders,
               horizontal_borders)  # ВЕРТИКАЛЬ

        Border(WIDTH * 0.12, HEGIHT * 0.179, WIDTH * 0.12, HEGIHT * 0.32, 'BLACK', sprites, vertical_borders,
               horizontal_borders)  # ВЕРТИКАЛЬ

    def main():
        pygame.init()
        birth()
        screen = pygame.display.set_mode((WIDTH, HEGIHT))
        dt = 0
        while True:
            clock = pygame.time.Clock()
            events = pygame.event.get()
            for e in events:
                if e.type == pygame.QUIT:
                    return

            pygame.draw.rect(screen, (60, 42, 20),
                             (WIDTH * 0.9 - 80, 440 - WIDTH * 0.115, WIDTH * 0.08, WIDTH * 0.1 + 10),
                             7)

            fon = pygame.image.load('data/fon_4.png')
            fon_rect = fon.get_rect(bottomright=(WIDTH, HEGIHT))
            screen.blit(fon, fon_rect)

            pygame.draw.rect(screen, (60, 42, 20), (WIDTH * 0.1 - 50, 60, WIDTH * 0.08, WIDTH * 0.1 + 10), 7)
            fon_2 = pygame.image.load('data/for 4 map.jpg')
            screen.blit(fon_2, (WIDTH * 0.1 - 50, 58))

            sprites.update(events, dt)
            sprites.draw(screen)
            pygame.display.update()
            dt = clock.tick(60)

    main()


if __name__ == '__main__':
    map_2(1, 2, 3, 1)