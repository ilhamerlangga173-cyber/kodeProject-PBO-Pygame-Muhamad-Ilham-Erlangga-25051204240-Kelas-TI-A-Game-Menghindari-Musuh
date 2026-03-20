import pygame
import random
import sys

pygame.init()

# ukuran layar
WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Menghindari Musuh")

font = pygame.font.SysFont(None, 36)
font_big = pygame.font.SysFont(None, 70)

# FPS
clock = pygame.time.Clock()

# warna
hijau = (0,255,0)
merah = (255,0,0)
putih = (255,255,255)


#class dasar
class GameObject:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)


class Player(GameObject):

    def __init__(self):
        self.x = WIDTH//2
        self.y = HEIGHT - 60 
        self.width = 40
        self.height = 40
        self.color = hijau
        self.speed = 5

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < WIDTH-self.width:
            self.x += self.speed


class Enemy(GameObject):

    def __init__(self):
        self.x = random.randint(0, WIDTH-30)
        self.y = 0
        self.width = 30
        self.height = 30
        self.color = merah
        self.speed = random.randint(2,5)

    def update(self):
        self.y += self.speed

        if self.y > HEIGHT:
            self.y = 0
            self.x = random.randint(0, WIDTH-self.width)
            return 1

        return 0


#tampilkan objek
player = Player()
enemies = [Enemy() for i in range(5)]

running = True
game_over = False
score = 0


#game loop
while running:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:

        keys = pygame.key.get_pressed()
        player.move(keys)

        for enemy in enemies:
            score += enemy.update()

            if player.get_rect().colliderect(enemy.get_rect()):
                game_over = True

    screen.fill((0,0,255))

    player.draw(screen)

    for enemy in enemies:
        enemy.draw(screen)

    score_text = font.render("Score: " + str(score), True, putih)
    screen.blit(score_text, (10,10))

    if game_over:
        gameover_text = font_big.render("GAME OVER", True, putih)
        screen.blit(gameover_text, (WIDTH//2- 160 , HEIGHT//2-30 ))

    pygame.display.update()

pygame.quit()
sys.exit()  