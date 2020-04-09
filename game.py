import pygame, random
import tkinter as tk
from tkinter import messagebox
from snake import snake
from cube import cube

width = 600
height = 600
rows = 20
flag = True


def drawGrid(surface):
    global width, height, rows
    sizeBtwn = width // rows
    x = 0
    y = 0

    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn
 
        pygame.draw.line(surface, (255,255,255), (x,0),(x, width))
        pygame.draw.line(surface, (255,255,255), (0,y),(width, y))

def redrawWindow(surface):
    global s, snack
    surface.fill((3, 5, 15))
    drawGrid(surface)
    s.draw(surface)
    snack.draw(surface)
    pygame.display.update()

def randomSnack(rows, item):
 
    positions = item.body
 
    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0:
            continue
        else:
            break
       
    return (x,y)

def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass

def main():
    global width, height, flag, s, snack
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Snake Game by TheRiolDeal")
    message_box("WELCOME", "Welcome to my game! \nClick Ok to Play \nHit R to restart whenever you want. \nEnjoy!:D")

    s = snake((7, 189, 85), (10, 10))
    snack = cube(randomSnack(rows, s), color=(240, 12, 12))

    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(60)
        clock.tick(8)
        redrawWindow(window)
        s.move()
        
        if s.body[0].pos == snack.pos:
            s.addCube()
            snack = cube(randomSnack(rows, s), color=(240, 12, 12))
        
        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z:z.pos,s.body[x+1:])):
                print('Score: ', len(s.body))
                message_box('You Lost! ', f'Score: , {len(s.body)} \nPlay again...')
                s.reset((10,10))
                break

main()