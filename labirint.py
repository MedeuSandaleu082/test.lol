# Разработай свою игру в этом файле!

import pygame

pygame.init()

WIDIH = 800
HEIGHT = 500

GREEN = (155,200, 155)

BLACK = (0, 0 , 0)

window = pygame.display.set_mode((WIDIH, HEIGHT))

BG = pygame.image.load('background.jpg')

BG = pygame.transform.scale(BG, (WIDIH, HEIGHT))

clock = pygame.time.Clock()

class Sprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (50, 55))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(Sprite):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= 3
        if keys[pygame.K_d]:
            self.rect.x += 3
        if keys[pygame.K_w]:
            self.rect.y -= 3
        if keys[pygame.K_s]:
            self.rect.y += 3
        
class Enemy(Sprite):
    def update(self):
        self.rect.x += self.dx
        if self.rect.x <= 460 or self.rect.x >= 700:
            self.dx = -self.dx
            
class Bot(Sprite):
    def __init__(self, image, x, y):
        super().__init__(image, x, y)
        self.dx = 2  

    def update(self):
        self.rect.x += self.dx
        if self.rect.x <= 460 or self.rect.x >= 700:
            self.dx = -self.dx

bot = Bot('cyborg.png', 600, 280)

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, WIDIH, HEIGHT):
        super().__init__()

        self.image = pygame.Surface((WIDIH, HEIGHT))
        self.image.fill(GREEN)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

def draw(self):
    window.blit(self.image, (self.rect.x, self.rect.y))

walls = pygame.sprite.Group()
walls.add(Wall(100, 20, 450, 10))
walls.add(Wall(100, 480, 350, 10))
walls.add(Wall(100, 20, 10, 380))
walls.add(Wall(200, 130, 10, 350))
walls.add(Wall(450, 130, 10, 360))
walls.add(Wall(300, 20, 10, 350))
walls.add(Wall(390, 120, 130, 10))



player = Player('hero.png', 5 , 100)
bot = Enemy('cyborg.png', 600, 280)
goal = Sprite('treasure.png', 580, 420)

bot.dx = 3

def restart():
    global paused, final
    player.rect.x = 5
    player.rect.y = 100
    paused = False
    final = False

pygame.mixer.music.load('jungles.ogg')
pygame.mixer.music.play()

kick = pygame.mixer.Sound('kick.ogg')
text_fin = None

run = True
paused = False
final = False

my_font = pygame.font.SysFont('verdana', 70)

text_pause =my_font.render('stop', True, BLACK)

text_win =my_font.render('WIN GAME', True, BLACK)

text_lose =my_font.render('GAME OVER', True, BLACK )

my_font = pygame.font.SysFont('verdana', 70)

text_restart =my_font.render('Press ESCAPE to restart', True, BLACK )

text_continue =my_font.render('Press ESCAPE to continue', True, BLACK )





while run:

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE and paused and final:
                restart()
            if e.key == pygame.K_ESCAPE and not final:
                paused = not paused

    if not paused:

        window.blit(BG, (0, 0))

        player.update()
        bot.update()
        
        player.draw()
        bot.draw()

        bot.update()
        bot.draw()
        goal.draw()
        walls.draw(window)

        if pygame.sprite.spritecollideany(player, walls) or pygame.sprite.collide_rect(player, bot):
            
            paused = True
            final = True
            text_fin = text_lose
            kick.play()

        if pygame.sprite.collide_rect(player, goal):
            paused = True
            final = True
            text_fin = text_win

    elif paused and final:
        window.fill(GREEN)
        window.blit(text_fin, (150, 200))
        window.blit(text_restart, (200, 150))

    elif paused and not final:
        window.fill(GREEN)
        window.blit(text_pause, (150, 200))
        window.blit(text_continue, (200, 150))

    pygame.display.update()

    clock.tick(60)

    