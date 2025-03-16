import pygame
import datetime

pygame.init()

def blitRotate(surf, image, center, angle):
        #Функция для поворота изображения       
        rotated_image = pygame.transform.rotate(image, angle)
        new_rect = rotated_image.get_rect(center=center)
        surf.blit(rotated_image, new_rect.topleft)

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
center = (400,300)
running = True

# Загрузка изображений
background = pygame.image.load("clock_images/clock.png")
minute_hand = pygame.image.load("clock_images/min_hand.png")
second_hand = pygame.image.load("clock_images/sec_hand.png")

# Масштабирование фона
background = pygame.transform.scale(background, (800, 600))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    # Получаем текущее время        
    now = datetime.datetime.now()
    minutes = now.minute
    seconds = now.second

    # Вычисляем угол поворота стрелок
    minute_angle = - (minutes * 6)
    second_angle = - (seconds * 6)

    screen.blit(background, (0,0))

    # Отрисовываем стрелки
    blitRotate(screen, minute_hand, center, minute_angle)
    blitRotate(screen, second_hand, center, second_angle)
    
    pygame.display.flip()
    clock.tick(60)
