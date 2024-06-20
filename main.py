import pygame
import random
from os.path import join


class Banana(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center=pos)
        self.start_time = pygame.time.get_ticks()
        self.lifetime = 3000
        self.direction = pygame.Vector2(random.uniform(-0.5, 0.5), 1)
        self.speed = 200
        self.can_shoot = True

    def update(self, dt):
        self.rect.center += self.direction * self.speed * dt
        if pygame.time.get_ticks() - self.start_time >= self.lifetime:
            self.kill()

        recent_keys = pygame.key.get_just_pressed()
        if recent_keys[pygame.K_c] and self.can_shoot:
            ShootCherry(cherry_surf, self.rect.midtop, all_sprites)


class ShootCherry(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(midbottom = pos)

    def update(self, dt):
        self.rect.centery += 400 * dt
        if self.rect.bottom < 0:
            self.kill()

class Grapes(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center=pos)
        self.start_time = pygame.time.get_ticks()
        self.lifetime = 3000
        self.direction = pygame.Vector2(random.uniform(-0.5, 0.5), 1)
        self.speed = 200

    def update(self, dt):
        self.rect.center += self.direction * self.speed * dt
        if pygame.time.get_ticks() - self.start_time >= self.lifetime:
            self.kill()

class Apple(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center=pos)
        self.start_time = pygame.time.get_ticks()
        self.lifetime = 3000
        self.direction = pygame.Vector2(random.uniform(-0.5, 0.5), 1)
        self.speed = 200

    def update(self, dt):
        self.rect.center += self.direction * self.speed * dt
        if pygame.time.get_ticks() - self.start_time >= self.lifetime:
            self.kill()

class Watermelon(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center=pos)
        self.start_time = pygame.time.get_ticks()
        self.lifetime = 3000
        self.direction = pygame.Vector2(random.uniform(-0.5, 0.5), 1)
        self.speed = 200

    def update(self, dt):
        self.rect.center += self.direction * self.speed * dt
        if pygame.time.get_ticks() - self.start_time >= self.lifetime:
            self.kill()

# General setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
running = True
clock = pygame.time.Clock()
pygame.display.set_caption("Fruit fall!")

# Import surf
banana_surf = pygame.image.load(join('Fruites', 'Banana.png')).convert_alpha()
grapes_surf = pygame.image.load(join('Fruites', 'Grapes.png')).convert_alpha()
apple_surf = pygame.image.load(join('Fruites', 'Apple.png')).convert_alpha()
watermelon_surf = pygame.image.load(join('Fruites', 'Watermelon.png')).convert_alpha()
cherry_surf = pygame.image.load(join('Fruites', 'Cherry.png')).convert_alpha()

# Sprites
all_sprites = pygame.sprite.Group()

# Custom Event
apple_event = pygame.event.custom_type()
pygame.time.set_timer(apple_event, 400)

banana_event = pygame.event.custom_type()
pygame.time.set_timer(banana_event, 500)

grape_event = pygame.event.custom_type()
pygame.time.set_timer(grape_event, 600)

watermelon_event = pygame.event.custom_type()
pygame.time.set_timer(watermelon_event, 700)


while running:
    dt = clock.tick() / 100

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == banana_event:
            x, y = random.randint(0, WINDOW_WIDTH), random.randint(-200, -100)
            Banana(banana_surf, (x, y), all_sprites)
        if event.type == grape_event:
            x, y = random.randint(0, WINDOW_WIDTH), random.randint(-200, -100)
            Grapes(grapes_surf, (x, y), all_sprites)
        if event.type == apple_event:
            x, y = random.randint(0, WINDOW_WIDTH), random.randint(-200, -100)
            Apple(apple_surf, (x, y), all_sprites)
        if event.type == watermelon_event:
            x, y = random.randint(0, WINDOW_WIDTH), random.randint(-200, -100)
            Watermelon(watermelon_surf, (x, y), all_sprites)


    all_sprites.update(dt)

    # Draw the game
    display_surface.fill('white')
    all_sprites.draw(display_surface)

    pygame.display.update()

pygame.quit()
