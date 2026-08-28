import pygame
import random
from settings import *


class Dinosaur(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((40, 60))
        self.image.fill(BLACK)

        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.bottom = HEIGHT - 50

        self.velocity_y = 0
        self.is_jumping = False

    def jump(self):
        if not self.is_jumping:
            self.velocity_y = JUMP_SPEED
            self.is_jumping = True

    def update(self):
        self.velocity_y += GRAVITY
        self.rect.y += self.velocity_y

        if self.rect.bottom >= HEIGHT - 50:
            self.rect.bottom = HEIGHT - 50
            self.velocity_y = 0
            self.is_jumping = False


class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        width = random.choice([20, 30, 40])
        height = random.choice([40, 60, 80])

        self.image = pygame.Surface((width, height))
        self.image.fill((255, 0, 0))

        self.rect = self.image.get_rect()
        self.rect.x = WIDTH + random.randint(0, 200)
        self.rect.bottom = HEIGHT - 50

    def update(self):
        self.rect.x -= GAME_SPEED

        if self.rect.right < 0:
            self.kill()


class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((WIDTH, 10))
        self.image.fill(GRAY)

        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = HEIGHT - 50
