print()

def map_3(pl1, pl11, pl2, pl22):
    import pygame
    from math import cos, sin, radians
    from classes import Player1, Projectile, Border, Player2

    WIDTH = 1000
    HEGIHT = 500

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
        Border(WIDTH * 0.4, HEGIHT * 0.18, WIDTH * 0.57, HEGIHT * 0.18, 'WHITE', sprites, vertical_borders,
               horizontal_borders)  # ГОРИЗОНТ
        Border(WIDTH * 0.3, HEGIHT * 0.3, WIDTH * 0.3, HEGIHT * 0.6, 'WHITE', sprites, vertical_borders,
               horizontal_borders)  # ВЕРТИКАЛЬ

        Border(WIDTH * 0.4, HEGIHT * 0.8, WIDTH * 0.57, HEGIHT * 0.8, 'WHITE', sprites, vertical_borders,
               horizontal_borders)  # ГОРИЗОНТ
        Border(WIDTH * 0.68, HEGIHT * 0.4, WIDTH * 0.68, HEGIHT * 0.7, 'WHITE', sprites, vertical_borders,
               horizontal_borders)  # ВЕРТИКАЛЬ

        Border(WIDTH * 0.4, HEGIHT * 0.4, WIDTH * 0.57, HEGIHT * 0.4, 'WHITE', sprites, vertical_borders,
               horizontal_borders)  # ГОРИЗОНТ
        Border(WIDTH * 0.4, HEGIHT * 0.6, WIDTH * 0.57, HEGIHT * 0.6, 'WHITE', sprites, vertical_borders,
               horizontal_borders)  # ГОРИЗОНТ

        Border(WIDTH * 0.18, HEGIHT * 0.11, WIDTH * 0.18, HEGIHT * 0.31, 'WHITE', sprites, vertical_borders,
               horizontal_borders)  # ВЕРТИКАЛЬ
        Border(WIDTH * 0.1, HEGIHT * 0.31, WIDTH * 0.19, HEGIHT * 0.31, 'WHITE', sprites, vertical_borders,
               horizontal_borders)  # ГОРИЗОНТ

        Border(WIDTH * 0.81, HEGIHT * 0.7, WIDTH * 0.81, HEGIHT * 0.9, 'WHITE', sprites, vertical_borders,
               horizontal_borders)  # ВЕРТИКАЛЬ
        Border(WIDTH * 0.81, HEGIHT * 0.7, WIDTH * 0.92, HEGIHT * 0.7, 'WHITE', sprites, vertical_borders,
               horizontal_borders)  # ГОРИЗОНТ

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
            fon = pygame.image.load('data/fon_3.png')
            fon_rect = fon.get_rect(bottomright=(1000, 500))
            screen.blit(fon, fon_rect)

            sprites.update(events, dt)
            sprites.draw(screen)
            pygame.display.update()
            dt = clock.tick(60)

    main()


if __name__ == '__main__':
    map_3(1, 2, 3, 2)
