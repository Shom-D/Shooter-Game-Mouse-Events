import pgzrun
import random

WIDTH, HEIGHT= 600,600
TITLE= 'Teleporting alien'

alien= Actor("junimo")
alien.pos= (300,300)
message= ""


def moving():
    alien.x = random.randint(50,WIDTH-50)
    alien.y = random.randint(50,HEIGHT-50)


def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        moving()
        message= "Yippee"
    else:
        message = "Better luck next time :("
        
    

def draw():
    screen.clear()
    screen.fill(color=(150,150,250))
    alien.draw()
    screen.draw.text(message, center= (WIDTH/2, 100))
    
    
    
    
pgzrun.go()

