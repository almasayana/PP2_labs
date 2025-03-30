import pygame
import random

pygame.init()

# Определение размеров окна и ячейки
WIDTH = 600  # Ширина экрана
HEIGHT = 600  # Высота экрана
CELL = 30  # Размер одной ячейки (квадрата)

# Определение цветов
colorWHITE = (255, 255, 255)
colorGRAY = (200, 200, 200)
colorBLACK = (0, 0, 0)
colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0)
colorYELLOW = (255, 255, 0)

# Создаем окно игры
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")


def draw_grid_chess():
    """Рисует шахматное поле"""
    colors = [colorWHITE, colorGRAY]
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))


class Point:
    """Класс, представляющий координаты (x, y)"""
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Snake:
    """Класс змейки"""
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]  # Начальные координаты змейки
        self.dx = 1  # Направление движения по X
        self.dy = 0  # Направление движения по Y
        self.score = 0  # Счет
        self.level = 1  # Уровень
        self.food_count = 0  # Количество съеденной еды

    def move(self):
        """Перемещение тела змейки"""
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        # Двигаем голову змейки в направлении движения
        self.body[0].x += self.dx
        self.body[0].y += self.dy

        # Обрабатываем выход за границы экрана (телепортируем змейку на другую сторону)
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

    def check_self_collision(self):
        """Проверяет, врезалась ли змея в саму себя"""
        head = self.body[0]
        for segment in self.body[1:]:
            if head.x == segment.x and head.y == segment.y:
                return True
        return False

    def check_collision(self, food):
        """Проверяет, съела ли змея еду"""
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            self.body.append(Point(head.x, head.y))  # Добавляем сегмент к змейке
            food.rand_pos()  # Перемещаем еду
            self.score += random.randint(5, 15)  # Увеличиваем счет
            self.food_count += 1

            # Каждые 3 съеденных еды увеличиваем уровень
            if self.food_count % 3 == 0:
                self.level += 1
                return True
        return False


class Food:
    """Класс еды"""
    def __init__(self):
        self.pos = Point(random.randint(0, WIDTH // CELL - 1), random.randint(0, HEIGHT // CELL - 1))
        self.timer = pygame.time.get_ticks()  # Запоминаем время появления еды

    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def rand_pos(self):
        """Перемещает еду в случайное место и сбрасывает таймер"""
        while True:
            new_pos = Point(random.randint(0, WIDTH // CELL - 1), random.randint(0, HEIGHT // CELL - 1))
            if not any(segment.x == new_pos.x and segment.y == new_pos.y for segment in snake.body):
                self.pos = new_pos
                self.timer = pygame.time.get_ticks()  # Обновляем таймер
                break

    def update_timer(self, time_limit=6000):  # Время в миллисекундах 
        """Если прошло время, перемещает еду"""
        if pygame.time.get_ticks() - self.timer > time_limit:
            self.rand_pos()


# Инициализация игры
FPS = 5  
clock = pygame.time.Clock()
snake = Snake()
food = Food()
running = True

while running:
    screen.fill(colorWHITE)
    
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
    food.update_timer()  # Проверяем таймер еды

    if snake.check_self_collision():
        font = pygame.font.SysFont(None, 100)
        text = font.render("Game Over!", True, colorRED)
        screen.blit(text, (WIDTH // 5, HEIGHT // 3))
        pygame.display.flip()
        pygame.time.delay(2000)
        running = False
        continue

    if snake.check_collision(food):
        FPS += 1

    snake.draw()
    food.draw()

    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {snake.score}  Level: {snake.level}", True, colorBLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
