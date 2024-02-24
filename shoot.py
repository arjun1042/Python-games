import pgzrun

from random import randint

apple = Actor("apple")

kiwi = Actor("kiwi")

def draw():
    
    screen.clear()
    apple.draw()
    kiwi.draw()
    
def place_kiwi():
    kiwi.x = randint(10,400)
    kiwi.y = randint(10,300)

def place_apple():
    apple.x = randint(10,400)
    apple.y = randint(10,300)

def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print("Good shot!")
        place_apple()

    elif kiwi.collidepoint(pos):
        print("Choose apple...")
        place_kiwi()
        

    else:
        print("You missed!\n")
        print("Game ended! \n Thank you for playing........")
        quit()

place_apple()

place_kiwi()

pgzrun.go()
