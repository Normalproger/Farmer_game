import os
import sys

import pygame as pygame

pygame.init()
width = 850
height = 550
size = 850, 550
screen = pygame.display.set_mode(size)


############################ Загрузка и обработка изображения ################################
def load_image(name, colorkey=None):
    fullname = os.path.join('backside', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


fon = pygame.transform.scale(load_image('back.jpg'), (width, height))
screen.blit(fon, (0, 0))

###################################### Создаем меню ############################################

Arial = pygame.font.SysFont('arial', 45)


class Menu:
    def __init__(self):
        self.x = None
        self.option_surfaces = []
        self.callbacks = []
        self.last_option_index = 0

    def append_option(self, sth_new, callback):
        self.option_surfaces.append(Arial.render(sth_new, True, 'White'))
        self.callbacks.append(callback)

    def switch(self, direction):
        self.last_option_index = max(0, min(self.last_option_index + direction, len(self.option_surfaces) - 1))

    def select(self):
        self.callbacks[self.last_option_index]()

    def draw(self, surface, x, y, padding):
        self.x = x
        for index, option in enumerate(self.option_surfaces):
            option_rect = option.get_rect()
            option_rect.topleft = (self.x, y + index * padding)
            if index == self.last_option_index:
                pygame.draw.rect(surface, 'black', option_rect, 3)
            else:
                pygame.draw.rect(surface, 'grey', option_rect, 1)
            surface.blit(option, option_rect)

    def update(self):



menu = Menu()
menu.append_option('Начать игру', lambda: print('heu'))
menu.append_option('выход', quit)

##################################### Основной игровой цикл #####################################
running = True

while running:
    x = 320
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                menu.switch(-1)
            elif event.key == pygame.K_DOWN:
                menu.switch(1)
            elif event.key == pygame.K_RETURN:
                menu.select()
                x += 700
    menu.draw(screen, x, 300, 50)
    pygame.display.flip()
quit()
