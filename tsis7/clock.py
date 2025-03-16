import pygame 
import time

pygame.init()

# Устанавливаем размеры окна
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
pygame.display.set_caption("Mickey Clock")

# Загружаем изображения
leftarm = pygame.image.load("clock_images/leftarm.png")  
rightarm = pygame.image.load("clock_images/rightarm.png") 
mainclock = pygame.transform.scale(pygame.image.load("clock_images/clock.png"), (800, 600))  

running = True

while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Получаем текущее время 
    current_time = time.localtime()
    minute = current_time.tm_min
    second = current_time.tm_sec
    
    # Вычисляем углы поворота стрелок
    minute_angle = minute * 6 + (second / 60) * 6
    second_angle = second * 6  
    
    screen.blit(mainclock, (0, 0))
    
    # Вращаем минутную стрелку
    rotated_rightarm = pygame.transform.rotate(pygame.transform.scale(rightarm, (800, 600)), -minute_angle)
    rightarmrect = rotated_rightarm.get_rect(center=(800 // 2, 600 // 2 + 12))
    screen.blit(rotated_rightarm, rightarmrect)
    
    # Вращаем секундную стрелку
    rotated_leftarm = pygame.transform.rotate(pygame.transform.scale(leftarm, (40.95, 682.5)), -second_angle)
    leftarmrect = rotated_leftarm.get_rect(center=(800 // 2, 600 // 2 + 10))
    screen.blit(rotated_leftarm, leftarmrect)
    
    pygame.display.flip() 
    clock.tick(60)  
