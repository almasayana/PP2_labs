import pygame
import random

pygame.init()

WIDTH = 600
HEIGHT = 600
CELL = 30

# Определение цветов
colorWHITE = (255, 255, 255)
colorGRAY = (200, 200, 200)
colorBLACK = (0, 0, 0)
colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0)
colorYELLOW = (255, 255, 0)

screen = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("Snake Game")


def draw_grid():
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)

# Функция для рисования шахматного фона

def draw_grid_chess():
    colors = [colorWHITE, colorGRAY]
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

# Класс точки 
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Класс змейки
class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]  # Начальное положение змейки
        self.dx = 1  # Направление движения по X
        self.dy = 0  # Направление движения по Y
        self.score = 0  # Очки игрока
        self.level = 1  # Уровень игры
        self.food_count = 0  # Количество съеденной еды

    def move(self):
        """Перемещение тела змейки """
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y
        
        # Двигаем голову змейки
        self.body[0].x += self.dx
        self.body[0].y += self.dy

        # Проверяем границы экрана и телепортируем змейку на противоположную сторону
        if self.body[0].x > WIDTH // CELL - 1:
            self.body[0].x = 0
        elif self.body[0].x < 0:
            self.body[0].x = WIDTH // CELL - 1
        if self.body[0].y > HEIGHT // CELL - 1:
            self.body[0].y = 0
        elif self.body[0].y < 0:
            self.body[0].y = HEIGHT // CELL - 1

    def draw(self):
        """Рисуем змею на экране"""
        pygame.draw.rect(screen, colorRED, (self.body[0].x * CELL, self.body[0].y * CELL, CELL, CELL)) 
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL)) 

    def check_collision(self, food):
        """Проверяем, съела ли змея еду"""
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            self.body.append(Point(head.x, head.y)) 
            food.rand_pos()
            self.score += 10  # Увеличиваем счет
            self.food_count += 1  # Увеличиваем счетчик съеденной еды
            
            if self.food_count % 3 == 0:
                self.level += 1
                return True  # уровень повысился
        return False

# Класс еды
class Food:
    def __init__(self):
        self.pos = Point(random.randint(0, WIDTH // CELL - 1), random.randint(0, HEIGHT // CELL - 1))

    def draw(self):
        """Рисуем еду на экране."""
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def rand_pos(self):
        """Перемещаем еду в случайное место"""
        while True:
            new_pos = Point(random.randint(0, WIDTH // CELL - 1), random.randint(0, HEIGHT // CELL - 1))
            if not any(segment.x == new_pos.x and segment.y == new_pos.y for segment in snake.body):
                self.pos = new_pos
                break

# Инициализация игры
FPS = 5  # Начальная скорость игры
clock = pygame.time.Clock()
snake = Snake()
food = Food()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.dx == 0:
                snake.dx = 1
                snake.dy = 0
            elif event.key == pygame.K_LEFT and snake.dx == 0:
                snake.dx = -1
                snake.dy = 0
            elif event.key == pygame.K_DOWN and snake.dy == 0:
                snake.dx = 0
                snake.dy = 1
            elif event.key == pygame.K_UP and snake.dy == 0:
                snake.dx = 0
                snake.dy = -1
    
    draw_grid_chess()
    snake.move()
    
    # Проверяем, съела ли змейка еду
    if snake.check_collision(food):
        FPS += 1  # Увеличиваем скорость при переходе на следующий уровень
    
    snake.draw()
    food.draw()
    
    # Отображение счета и уровня
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {snake.score}  Level: {snake.level}", True, colorBLACK)
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()