import pygame

class cube(object):
    rows = 20
    w = 600

    def __init__(self,start,directionx=1,directiony=0,color=(255,0,0)):
        self.pos = start
        self.directionx = 1
        self.directiony = 0
        self.color = color
 
       
    def move(self, directionx, directiony):
        self.directionx = directionx
        self.directiony = directiony
        self.pos = (self.pos[0] + self.directionx, self.pos[1] + self.directiony)
 
    def draw(self, surface, eyes=False):
        dis = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]
 
        pygame.draw.rect(surface, self.color, (i*dis+1,j*dis+1, dis-2, dis-2))
        if eyes:
            centre = dis//2
            radius = 3
            circleMiddle = (i*dis+centre-radius,j*dis+8)
            circleMiddle2 = (i*dis + dis -radius*2, j*dis+8)
            pygame.draw.circle(surface, (0,0,0), circleMiddle, radius)
            pygame.draw.circle(surface, (0,0,0), circleMiddle2, radius)