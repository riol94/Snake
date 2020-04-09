from cube import cube
import pygame

class snake(object):

    body = []
    turns = {}

    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos, color = color)
        self.body.append(self.head)
        self.directionx = 1
        self.directiony = 0

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT] and self.directionx != 1:
                    self.directionx = -1
                    self.directiony = 0
                    self.turns[self.head.pos[:]] = [self.directionx, self.directiony]

                elif keys[pygame.K_RIGHT] and self.directionx != -1:
                    self.directionx = 1
                    self.directiony = 0
                    self.turns[self.head.pos[:]] = [self.directionx, self.directiony]
                    
                elif keys[pygame.K_UP] and self.directiony != 1:
                    self.directionx = 0
                    self.directiony = -1
                    self.turns[self.head.pos[:]] = [self.directionx, self.directiony]

                elif keys[pygame.K_DOWN] and self.directiony != -1:
                    self.directionx = 0
                    self.directiony = 1
                    self.turns[self.head.pos[:]] = [self.directionx, self.directiony]
                
                elif keys[pygame.K_r]:
                    self.reset((10,10))
        
        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0],turn[1])
                if i == len(self.body)-1:
                    self.turns.pop(p)
            else:
                if c.directionx == -1 and c.pos[0] <= 0: c.pos = (c.rows-1, c.pos[1])
                elif c.directionx == 1 and c.pos[0] >= c.rows-1: c.pos = (0,c.pos[1])
                elif c.directiony == 1 and c.pos[1] >= c.rows-1: c.pos = (c.pos[0], 0)
                elif c.directiony == -1 and c.pos[1] <= 0: c.pos = (c.pos[0],c.rows-1)
                else: c.move(c.directionx,c.directiony)

    def addCube(self):
        tail = self.body[-1]
        dx, dy = tail.directionx, tail.directiony
 
        if dx == 1 and dy == 0:
            self.body.append(cube((tail.pos[0]-1,tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(cube((tail.pos[0]+1,tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(cube((tail.pos[0],tail.pos[1]-1)))
        elif dx == 0 and dy == -1:
            self.body.append(cube((tail.pos[0],tail.pos[1]+1)))
 
        self.body[-1].directionx = dx
        self.body[-1].directiony = dy
    
    def reset(self, pos):
        self.head = cube(pos, color = self.color)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.directionx = 1
        self.directiony = 0

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i ==0:
                c.draw(surface, True)
            else:
                c.draw(surface)