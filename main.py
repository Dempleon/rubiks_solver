import pygame
from pygame.locals import *

#face will take in a 3x3 array
class Face:
    def __init__(self, face):
        self.center = face[1][1]
        

class Cube:
    def __init__(self):
        self.white_face = [['white', 'white', 'white'],
                           ['white', 'white', 'white'],
                           ['white', 'white', 'white']]
        self.red_face = [['red', 'red', 'red'],
                         ['red', 'red', 'red'],
                         ['red', 'red', 'red']]
        self.blue_face = [['blue', 'blue', 'blue'],
                          ['blue', 'blue', 'blue'],
                          ['blue', 'blue', 'blue']]
        self.orange_face = [['orange', 'orange', 'orange'],
                            ['orange', 'orange', 'orange'],
                            ['orange', 'orange', 'orange']]
        self.green_face = [['green', 'green', 'green'],
                           ['green', 'green', 'green'],
                           ['green', 'green', 'green']]
        self.yellow_face = [['yellow', 'yellow', 'yellow'],
                            ['yellow', 'yellow', 'yellow'],
                            ['yellow', 'yellow', 'yellow']]

def view(cube):
    pass

def draw(window, cube):
    pass

def main():
    print('This is a rubiks cube solver project')
    pygame.init()
    window = pygame.display.set_mode((500, 500))
    clock = pygame.time.Clock()

    running = True
    cube = Cube()

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                print('**quitting program')
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    print('**quitting program')
                    running = False

        draw(window, cube)
        pygame.display.update()
        clock.tick(30)




if __name__ == '__main__':
    main()