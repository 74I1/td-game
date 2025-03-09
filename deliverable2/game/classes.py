
#speed = 5
#health = 10
#attack = 2
import time
import pygame
#screen = pygame.display.set_mode((1280, 720))

class enemy:
    def __init__(self,name,speed,attack, drop):   #the default framework for the enemy class with name, move speed, attack damage and drops
        self.name = name
        self.speed = speed
        self.attack = attack
        self.drop = drop
        #self.sprite = sprite
class Blocks:
    def __init__(self,name,health,cost):      # the default framework for the placibles class with name, health, abd cost
        self.name = name
        self.health = health
        self.cost = cost

class Triangle(enemy):
    def move_speed(self):        # the enemy triangel with the structure of the enemy class with set name, speed, attack, and drop
        None
   # def total_health(self):
    #    health += 0
    def total_attack(self):
        None
    def total_drop(self):
        None
    #def Triangle_sprite(self):
     #   pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(30, 30, 60, 60)) 
     
     
        
class Square(Blocks):
    def total_health(self):
        health += 20
    def total_cost(self):
        cost += 5

class Circle(enemy):
    def move_speed(self):
        speed += 5
    def total_attack(self):
        attack += 2
    def total_drop(self):
        drop += 2
    #def Circle_sprite(self):
     #   pygame.draw.rect(screen, (0, 128, 0), pygame.Rect(30, 30, 60, 60))
   
class Rectangle(Blocks):
    def total_health(self):
        health += 50
    def total_cost(self):
        cost += 25

Rectangle = Blocks(Rectangle, 50, 25)  # testing the placible Rectangel, prints the health, cost, and name for the stats for Rectangel
print(Rectangle.cost)
print(Rectangle.health)
print(Rectangle.name)

Circle = enemy(Circle, 5, 2, 2)
print(Circle.name)
print(Circle.attack)
print(Circle.speed)
print(Circle.drop)

Triangle = enemy(Triangle, 3, 2, 1)
print(Triangle.name)
print(Triangle.speed)
print(Triangle.attack)
print(Triangle.drop)
        
Square = Blocks(Square, 20, 5)
print(Square.name)
print(Square.health)
print(Square.cost)        


XGlobal = 30
YGlobal = 30

z = 2








def Triangle_tile_left( XNew ):
    global XGlobal
    XGlobal = XNew - z          # z represents the enemy speed attribute    XGlobal represents the intital position        XNew represents the new position after the affect of the movement tiles
    print("done left")               # don't know why this executes twice
    return(XGlobal)             # XNew is subtracted twice by z
    

def Triangle_tile_right(XNew):
    global XGlobal
    XGlobal = XNew + z
    print("done right")
    return(XGlobal)


def Triangle_tile_up(YNew):
    global YGlobal
    YGlobal = YNew + z
    print("done up")
    return(YGlobal)

def Triangle_tile_down(YNew):
    global YGlobal
    YGlobal = YNew - z
    print("done down")
    return(YGlobal)
 
    
Triangle_tile_right(70)
Triangle_tile_left(70)
Triangle_tile_up(70)
Triangle_tile_down(70)

print (Triangle_tile_left(XGlobal), YGlobal )



'''
print (Triangle_tile_left( XGlobal  ) )
print (Triangle_tile_left( XGlobal  ) )  # repeated the code three times to test if the are consistant. 
print (Triangle_tile_left( XGlobal  ) )  # the value is subtracted twice on the initial print function but functions are then consistant with the second and third
'''