import pygame
import random
import time

pygame.init()

# Устанавливаем размеры экрана
WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Загружаем изображения
image_background = pygame.image.load('resources/AnimatedStreet.png')
image_player = pygame.image.load('resources/Player.png')
image_enemy = pygame.image.load('resources/Enemy.png')
image_coin = pygame.image.load('resources/coin.png')
image_coin = pygame.transform.scale(image_coin, (40, 40))  # Масштабируем изображение монеты

# Загружаем и воспроизводим фоновую музыку
pygame.mixer.music.load('resources/background.wav')
pygame.mixer.music.play(-1)

# Загружаем звук столкновения
sound_crash = pygame.mixer.Sound('resources/crash.wav')

# Настраиваем шрифты и текст "Game Over"
font = pygame.font.SysFont("Verdana", 60)
small_font = pygame.font.SysFont("Verdana", 30)
image_game_over = font.render("Game Over", True, "black")
image_game_over_rect = image_game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Счетчик собранных монет
COINS = 0

# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_player
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 50))
        self.speed = 4  # Скорость перемещения

    def move(self):
        keys = pygame.key.get_pressed()
        # Управление движением игрока
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed

# Класс врага
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_enemy
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = -self.rect.height  # Начальная позиция выше экрана
        self.speed = 5  # Скорость движения врага вниз

    def move(self):
        self.rect.y += self.speed
        # Если враг вышел за экран, перемещаем его наверх с новой случайной позицией
        if self.rect.top > HEIGHT:
            self.rect.x = random.randint(0, WIDTH - self.rect.width)
            self.rect.y = -self.rect.height

# Класс монет
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_coin
        self.rect = self.image.get_rect()
        self.spawn()
        self.speed = 3  # Скорость падения монеты

    def spawn(self):
        # Размещаем монету в случайной позиции сверху экрана
        self.rect.x = random.randint(20, WIDTH - 60)
        self.rect.y = -40

    def move(self):
        self.rect.y += self.speed  # Монета падает вниз
        if self.rect.top > HEIGHT:  # Если монета вышла за экран, создаем новую сверху
            self.spawn()

# Создаем объекты
player = Player()
enemy = Enemy()
coin = Coin()

# Создаем группы спрайтов
all_sprites = pygame.sprite.Group(player, enemy, coin)
enemy_sprites = pygame.sprite.Group(enemy)
coin_sprites = pygame.sprite.Group(coin)

clock = pygame.time.Clock()
FPS = 60
running = True

# Основной игровой цикл
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Двигаем объекты
    player.move()
    enemy.move()
    coin.move()
    
    # Отображаем фон
    screen.blit(image_background, (0, 0))
    
    # Отображаем все объекты
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
    
    # Проверяем столкновение игрока с врагом
    if pygame.sprite.spritecollideany(player, enemy_sprites):
        sound_crash.play()
        time.sleep(1)
        screen.fill("red")
        screen.blit(image_game_over, image_game_over_rect)
        pygame.display.flip()
        time.sleep(3)
        running = False  # Завершаем игру
    
    # Проверяем столкновение игрока с монетой
    if pygame.sprite.spritecollide(player, coin_sprites, True):
        COINS += 1  # Увеличиваем счетчик монет
        coin = Coin()
        all_sprites.add(coin)
        coin_sprites.add(coin)
    
    # Отображаем количество монет
    coin_text = small_font.render(f"Coins: {COINS}", True, "black")
    screen.blit(coin_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(FPS)  # Ограничиваем FPS

pygame.quit()
