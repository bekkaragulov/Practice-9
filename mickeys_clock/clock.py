import pygame
import datetime
import math
import os
import sys

pygame.init()

W, H = 600, 400
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Mickey Clock")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (239, 228, 176)

font = pygame.font.SysFont("Arial", 28, bold=True)
clock = pygame.time.Clock()

base = os.path.dirname(__file__)
img_path = os.path.join(base, "images")

# фон часов
face = pygame.image.load(os.path.join(img_path, "clock_face.png")).convert_alpha()
face = pygame.transform.scale(face, (W, H))

# руки (изображения)
right_hand = pygame.image.load(os.path.join(img_path, "right_hand.png")).convert_alpha()
left_hand = pygame.image.load(os.path.join(img_path, "left_hand.png")).convert_alpha()

# масштаб (можешь менять если нужно)
right_hand = pygame.transform.scale(right_hand, (600, 600))
left_hand = pygame.transform.scale(left_hand, (600, 600))

cx, cy = W // 2, H // 2


# функция вращения руки
def draw_hand(image, angle):
    rotated = pygame.transform.rotate(image, -angle)
    rect = rotated.get_rect(center=(cx, cy))
    screen.blit(rotated, rect)


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    now = datetime.datetime.now()

    h = now.hour % 12
    m = now.minute
    s = now.second

    # углы
    hour_angle = h * 30 + m * 0.5
    minute_angle = m * 6 + s * 0.1
    second_angle = s * 6

    screen.fill(WHITE)
    screen.blit(face, (0, 0))

    # часовая стрелка (оставим линией)
    angle_rad = math.radians(hour_angle - 90)
    hx = cx + 70 * math.cos(angle_rad)
    hy = cy + 70 * math.sin(angle_rad)
    pygame.draw.line(screen, BLACK, (cx, cy), (hx, hy), 6)

    # правая рука = минутная стрелка
    draw_hand(right_hand, minute_angle)

    # левая рука = секундная стрелка
    draw_hand(left_hand, second_angle)

    # центр
    pygame.draw.circle(screen, BLACK, (cx, cy), 6)

    # цифровое время
    text = font.render(now.strftime("%H:%M:%S"), True, RED, YELLOW)
    screen.blit(text, (430, 350))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()