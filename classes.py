from math import radians, sin, cos
import pygame


class Player1(pygame.sprite.Sprite):
    def __init__(self, borders_v, borders_h, x, y, type1, type2, mybuls, others, enemy):
        super().__init__()
        self.mybull = mybuls
        self.others = others
        self.borders_v = borders_v
        self.borders_h = borders_h
        self.x = x
        self.y = y
        self.pl = 1
        if type1 == 1:
            self.v = 4
            self.health = 10
            color = 'red'
        elif type1 == 2:
            color = 'dodgerblue'
            self.v = 6
            self.health = 7
        else:
            color = 'yellow'
            self.v = 7
            self.health = 5
        self.enemy = enemy
        if type2 == 1:
            self.gun_color = 'red'
            self.damage = 6
            self.lives = 5
            self.velocity = 7
        elif type2 == 2:
            self.gun_color = 'dodgerblue'
            self.damage = 4
            self.velocity = 6
            self.lives = 4
        else:
            self.gun_color = 'yellow'
            self.lives = 3
            self.damage = 3
            self.velocity = 5

        self.image = pygame.Surface((32, 32))
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        self.tank = pygame.draw.polygon(self.image, pygame.Color(color), ((0, 0),
                                                                                 (32, 16),
                                                                                 (0, 32)))
        self.org_image = self.image.copy()
        self.angle = 0
        self.direction = pygame.Vector2(1, 0)
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.pos = pygame.Vector2(self.rect.center)

    def add_enemy(self, en_group):
        self.en_group = en_group

    def update(self, events, dt):
        if self.health < 1:
            self.kill()
        for e in events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    self.groups()[0].add(Projectile(self.rect.center, self.direction.normalize(), self.borders_v,
                                                    self.borders_h, self.velocity, self.lives, self.damage, self.pl, self.mybull, self.en_group))
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_a]:
            self.angle += 3
        if pressed[pygame.K_d]:
            self.angle -= 3
        if pressed[pygame.K_w]:
            self.rect = self.rect.move(int(self.v * cos(radians(self.angle % 360))), int(self.v * -sin(radians(self.angle % 360))))

        if pygame.sprite.spritecollideany(self, self.borders_v) or pygame.sprite.spritecollideany(self, self.borders_h):
            self.v = 1.4
        else:
            self.v = 4
        if pygame.sprite.spritecollideany(self, self.others):
            self.health -= self.enemy.damage

        self.direction = pygame.Vector2(1, 0).rotate(-self.angle)
        self.image = pygame.transform.rotate(self.org_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

class Player2(pygame.sprite.Sprite):
    def __init__(self, borders_v, borders_h, x, y, type1, type2, mybuls, others, enemy):
        super().__init__()
        self.mybull = mybuls
        self.others = others
        self.borders_v = borders_v
        self.borders_h = borders_h
        self.x = x
        self.y = y
        self.pl = 2
        if type1 == 1:
            self.v = 4
            self.health = 10
            color = 'red'
        elif type1 == 2:
            color = 'dodgerblue'
            self.v = 6
            self.health = 7
        else:
            color = 'yellow'
            self.v = 7
            self.health = 5
        self.enemy = enemy
        if type2 == 1:
            self.gun_color = 'red'
            self.damage = 6
            self.lives = 5
            self.velocity = 7
        elif type2 == 2:
            self.gun_color = 'dodgerblue'
            self.damage = 4
            self.velocity = 6
            self.lives = 4
        else:
            self.gun_color = 'yellow'
            self.lives = 3
            self.damage = 3
            self.velocity = 5
        self.image = pygame.Surface((32, 32))
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        self.tank = pygame.draw.polygon(self.image, pygame.Color(color), ((0, 0),
                                                                                 (32, 16),
                                                                                 (0, 32)))
        self.org_image = self.image.copy()
        self.angle = 0
        self.direction = pygame.Vector2(1, 0)
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.pos = pygame.Vector2(self.rect.center)

    def add_enemy(self, en_group):
        self.en_group = en_group

    def update(self, events, dt):
        print(self.health)
        if self.health < 1:
            self.kill()
        for e in events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_m:
                    self.groups()[0].add(Projectile(self.rect.center, self.direction.normalize(), self.borders_v,
                                                    self.borders_h, self.velocity, self.lives, self.damage, self.pl,
                                                    self.mybull, self.en_group))
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            self.angle += 3
        if pressed[pygame.K_RIGHT]:
            self.angle -= 3
        if pressed[pygame.K_UP]:
            self.rect = self.rect.move(int(self.v * cos(radians(self.angle % 360))), int(self.v * -sin(radians(self.angle % 360))))

        if pygame.sprite.spritecollideany(self, self.borders_v) or pygame.sprite.spritecollideany(self, self.borders_h):
            self.v = 1.4
        else:
            self.v = 4

        if pygame.sprite.spritecollideany(self, self.others):
            self.health -= self.enemy.damage


        self.direction = pygame.Vector2(1, 0).rotate(-self.angle)
        self.image = pygame.transform.rotate(self.org_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)


class Projectile(pygame.sprite.Sprite):

    def __init__(self, pos, direction, v_borders, h_borders, velocity, lives, damage, pl, group, en_group):
        super().__init__()
        group.add(self)
        self.en_group = en_group
        self.v_borders = v_borders
        self.h_borders = h_borders
        self.damage = damage
        self.image = pygame.Surface((8, 8))
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        pygame.draw.circle(self.image, pygame.Color('white'), (4, 4), 4)
        self.rect = self.image.get_rect(center=pos)
        self.direction = direction
        self.pos = pygame.Vector2(self.rect.center)
        self.lives = lives
        self.v = velocity

    def update(self, events, dt):
        screen_r = pygame.display.get_surface().get_rect()
        # where we would move next
        next_pos = self.pos + self.direction * self.v
        # we hit a hall
        if pygame.sprite.spritecollideany(self, self.en_group):
            return self.kill()
        if self.lives < 1:
            self.kill()
        if pygame.sprite.spritecollideany(self, self.h_borders):
            self.direction.y *= -1
            self.lives -= 1
        if pygame.sprite.spritecollideany(self, self.v_borders):
            self.direction.x *= -1
            self.lives -= 1
        if not screen_r.contains(self.rect):
            # after 15 hits, destroy self
            self.lives -= 1
            if self.lives == 0:
                return self.kill()
            # horizontal reflection
            if next_pos.x > screen_r.right or next_pos.x < screen_r.left:
                self.direction.x *= -1
            # vertical reflection
            if next_pos.y > screen_r.bottom or next_pos.y < screen_r.top:
                self.direction.y *= -1
            # move after applying reflection

        next_pos = self.pos + self.direction * self.v
        # set the new position
        self.pos = next_pos
        self.rect.center = self.pos


class Border(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2, color, sprites_call, v_bord, h_bord):
        super().__init__(sprites_call)
        if x1 == x2:
            self.add(v_bord)
            self.image = pygame.Surface([10, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 10, y2 - y1)
            self.image.fill(color)
        else:
            self.add(h_bord)
            self.image = pygame.Surface([x2 - x1, 10])
            self.image.fill(color)
            self.rect = pygame.Rect(x1, y1, x2 - x1, 10)