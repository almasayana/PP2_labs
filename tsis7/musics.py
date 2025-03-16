import pygame
import os

pygame.init()

# Загрузка плейлиста
playlist = []
music_folder = "musics"
allmusic = os.listdir(music_folder)

for song in allmusic:
    if song.endswith(".mp3"):
        playlist.append(os.path.join(music_folder, song))

# Создание окна
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Lana Del Rey")
clock = pygame.time.Clock()

# Загрузка фона
background = pygame.image.load(os.path.join("music-elements", "lana-background.png"))
background = pygame.transform.scale(background, (800, 600))

# Фон для кнопок
bg = pygame.Surface((500, 150))
bg.fill((255, 228, 178))

# Шрифт
font2 = pygame.font.SysFont(None, 24)

# Загрузка кнопок
playb = pygame.image.load(os.path.join("music-elements", "play.png"))
pausb = pygame.image.load(os.path.join("music-elements", "pause.png"))
nextb = pygame.image.load(os.path.join("music-elements", "next.png"))
prevb = pygame.image.load(os.path.join("music-elements", "back.png"))

# Изменяем размер кнопок
playb = pygame.transform.scale(playb, (60, 60))
pausb = pygame.transform.scale(pausb, (60, 60))
nextb = pygame.transform.scale(nextb, (60, 60))
prevb = pygame.transform.scale(prevb, (60, 60))

index = 0
aplay = False

# Запуск первой песни
pygame.mixer.music.load(playlist[index])
pygame.mixer.music.play(1)
aplay = True

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if aplay:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
                aplay = not aplay

            if event.key == pygame.K_RIGHT:
                index = (index + 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()

            if event.key == pygame.K_LEFT:
                index = (index - 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()

    # Отрисовка фона
    screen.blit(background, (0, 0))
    screen.blit(bg, (150, 450))

    # Отображение названия песни
    text2 = font2.render(os.path.basename(playlist[index]), True, (20, 20, 50))
    screen.blit(text2, (280, 470))

    # Отображение кнопок
    screen.blit(pausb if aplay else playb, (370, 510))
    screen.blit(nextb, (460, 510))
    screen.blit(prevb, (280, 510))

    clock.tick(24)
    pygame.display.update()
