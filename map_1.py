WIDTH = 1000
HEGIHT = 500

print()

def map_1(pl1, pl11, pl2, pl22):
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
        Border(WIDTH * 0.400, HEGIHT * 0.15, WIDTH * 0.600, HEGIHT * 0.15, 'cyan', sprites, vertical_borders,
               horizontal_borders)
        Border(WIDTH * 0.400, HEGIHT * 0.85, WIDTH * 0.600, HEGIHT * 0.85, 'cyan', sprites, vertical_borders,
               horizontal_borders)

        Border(WIDTH * 0.25, 0, WIDTH * 0.25, HEGIHT * 0.15, 'black', sprites, vertical_borders, horizontal_borders)  #
        Border(WIDTH * 0.25, HEGIHT * 0.150, WIDTH * 0.30, HEGIHT * 0.15, 'black', sprites, vertical_borders,
               horizontal_borders)  #
        Border(WIDTH * 0.30, HEGIHT * 0.15, WIDTH * 0.300, HEGIHT * 0.30, 'black', sprites, vertical_borders,
               horizontal_borders)

        Border(WIDTH * 0.27, HEGIHT * 0.4, WIDTH * 0.30, HEGIHT * 0.5, 'red', sprites, vertical_borders,
               horizontal_borders)
        Border(WIDTH * 0.30, HEGIHT * 0.4, WIDTH * 0.30, HEGIHT * 0.6, 'red', sprites, vertical_borders,
               horizontal_borders)
        Border(WIDTH * 0.27, HEGIHT * 0.6, WIDTH * 0.31, HEGIHT * 0.6, 'red', sprites, vertical_borders,
               horizontal_borders)

        Border(WIDTH * 0.30, HEGIHT * 0.7, WIDTH * 0.30, HEGIHT * 0.85, 'black', sprites, vertical_borders,
               horizontal_borders)  #
        Border(WIDTH * 0.25, HEGIHT * 0.85, WIDTH * 0.31, HEGIHT * 0.85, 'black', sprites, vertical_borders,
               horizontal_borders)  #
        Border(WIDTH * 0.25, HEGIHT * 0.85, WIDTH * 0.25, HEGIHT, 'black', sprites, vertical_borders,
               horizontal_borders)  #

        Border(WIDTH * 0.07, HEGIHT * 0.4, WIDTH * 0.10, HEGIHT * 0.5, 'blue', sprites, vertical_borders,
               horizontal_borders)
        Border(WIDTH * 0.10, HEGIHT * 0.4, WIDTH * 0.10, HEGIHT * 0.6, 'blue', sprites, vertical_borders,
               horizontal_borders)
        Border(WIDTH * 0.07, HEGIHT * 0.6, WIDTH * 0.11, HEGIHT * 0.6, 'blue', sprites, vertical_borders,
               horizontal_borders)

        Border(WIDTH * 0.5, HEGIHT * 0.4, WIDTH * 0.5, HEGIHT * 0.6, 'black', sprites, vertical_borders,
               horizontal_borders)

        Border(WIDTH * 0.7, HEGIHT * 0.15, WIDTH * 0.7, HEGIHT * 0.3, 'black', sprites, vertical_borders,
               horizontal_borders)
        Border(WIDTH * 0.7, HEGIHT * 0.15, WIDTH * 0.76, HEGIHT * 0.15, 'black', sprites, vertical_borders,
               horizontal_borders)
        Border(WIDTH * 0.75, 0, WIDTH * 0.75, HEGIHT * 0.15, 'black', sprites, vertical_borders, horizontal_borders)  #

        Border(WIDTH * 0.75, HEGIHT * 0.85, WIDTH * 0.75, HEGIHT, 'black', sprites, vertical_borders,
               horizontal_borders)
        Border(WIDTH * 0.7, HEGIHT * 0.85, WIDTH * 0.75, HEGIHT * 0.85, 'black', sprites, vertical_borders,
               horizontal_borders)
        Border(WIDTH * 0.7, HEGIHT * 0.7, WIDTH * 0.7, HEGIHT * 0.85, 'black', sprites, vertical_borders,
               horizontal_borders)

        Border(WIDTH * 0.7, HEGIHT * 0.4, WIDTH * 0.73, HEGIHT * 0.4, 'red', sprites, vertical_borders,
               horizontal_borders)
        Border(WIDTH * 0.7, HEGIHT * 0.4, WIDTH * 0.7, HEGIHT * 0.6, 'red', sprites, vertical_borders,
               horizontal_borders)
        Border(WIDTH * 0.7, HEGIHT * 0.6, WIDTH * 0.73, HEGIHT * 0.6, 'red', sprites, vertical_borders,
               horizontal_borders)

        Border(WIDTH * 0.9, HEGIHT * 0.4, WIDTH * 0.93, HEGIHT * 0.4, 'blue', sprites, vertical_borders,
               horizontal_borders)
        Border(WIDTH * 0.9, HEGIHT * 0.4, WIDTH * 0.9, HEGIHT * 0.6, 'blue', sprites, vertical_borders,
               horizontal_borders)
        Border(WIDTH * 0.9, HEGIHT * 0.6, WIDTH * 0.93, HEGIHT * 0.6, 'blue', sprites, vertical_borders,
               horizontal_borders)

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
            screen.fill('white')

            fon = pygame.image.load('data/fon.png')
            fon_rect = fon.get_rect(bottomright=(WIDTH, HEGIHT))
            screen.blit(fon, fon_rect)

            sprites.update(events, dt)
            sprites.draw(screen)
            pygame.display.update()
            dt = clock.tick(60)

    main()


if __name__ == '__main__':
    map_1(1, 2, 3, 1)
