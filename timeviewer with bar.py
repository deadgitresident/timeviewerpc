import pygame
import time
import sys

from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((512, 1024), pygame.SCALED | pygame.FULLSCREEN)
pygame.display.set_caption('Time Load')

main_font = 'arial'

def display_time(main_time):
    font = pygame.font.SysFont(main_font, 85)
    time_surface = font.render(str(main_time), True, (255, 255, 255))
    time_rect = time_surface.get_rect()
    time_rect.center = screen.get_rect().center
    screen.blit(time_surface, time_rect)

def display_date(main_date):
    font = pygame.font.SysFont(main_font, 25)
    date_surface = font.render(str(main_date), True, (255, 255, 255))
    date_rect = date_surface.get_rect()
    date_rect.center = screen.get_rect().center
    date_rect.top = screen.get_rect().center[1] + 50
    screen.blit(date_surface, date_rect)

def show_name(name, shifty=0):
    font = pygame.font.SysFont(main_font, 35)
    name_surface = font.render(name, True, (255, 255, 255))
    name_rect = name_surface.get_rect()
    name_rect.center = screen.get_rect().center
    name_rect.top = 300 + shifty
    screen.blit(name_surface, name_rect)

def progress_bar(h_ratio, default=24, shifty=0):
    h_ratio = int(h_ratio)
    rect = pygame.Rect(0, 0, screen.get_width() - 100, 10)
    rect.center = screen.get_rect().center
    rect.bottom = screen.get_height() - 300 + shifty

    r = (h_ratio / default) * 100
    r = r / 100 * rect[2]
    pygame.draw.rect(screen, (70, 70, 70), rect, 0)
    pygame.draw.rect(screen, (200, 200, 200), (rect[0], rect[1], r, rect[3]))

def conv_time():
    _time = time.localtime()
    current_time = time.asctime(_time)
    return current_time

def exit_game():
    pygame.quit()
    sys.exit()

def main():
    quit = False
    while not quit:
        for ev in pygame.event.get():
            if ev.type == QUIT:
                quit = True

        screen.fill((0, 0, 0))
        _time = conv_time()
        display_time(_time[-13:-4])
        display_date(_time[:-13])
        progress_bar(int(_time[-13:-11]))
        progress_bar(int(_time[-10:-8]), default=60, shifty=15)
        progress_bar(int(_time[-7:-5]), default=60, shifty=30)
        pygame.display.update()

    exit_game()

if __name__ == "__main__":
    main()