import pgzrun

WIDTH, HEIGHT, TITLE =600, 600, 'Shooter'

bullet= Actor("bullet")
gun= Actor("gun")
alien= Actor("junimo")
message=""

gun.pos =(100,300)
bullet.pos= gun.pos
alien.pos=(500,300)


def checker():
    global message
    while True:
        bullet.x +=1
        if bullet.x==600:
            message="You missed :("
            break
        elif alien.collidepoint(bullet.pos):
            message="Yay"
            break
    


def on_mouse_down(pos):
    bullet.draw()
    checker()
    



def draw():
    screen.clear()
    screen.fill(color=(150,150,250))
    gun.draw()
    alien.draw()
    bullet.draw()
    screen.draw.text(message, center= (WIDTH/2, 100))



pgzrun.go()