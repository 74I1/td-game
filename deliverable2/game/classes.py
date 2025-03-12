

#speed = 5
#health = 10
#attack = 2
import time
#import pygame
#screen = pygame.display.set_mode((1280, 720))

class enemy:
    def __init__(self,name,speed,attack, drop):   #the default framework for the enemy class with name, move speed, attack damage and drops
        self.name = name                          # enemies should also have sprite boxes which work withh the Collistion functions
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









def Triangle_tile_left( XNew ):
    global XGlobal
    XGlobal = XNew - Triangle.speed        # Triangle.speed represents the enemy speed attribute    XGlobal represents the intital position        XNew represents the new position after the affect of the movement tiles
   # print("done left")               
    return(XGlobal)             # XNew is subtracted by Triangle.speed
    

def Triangle_tile_right(XNew):
    global XGlobal
    XGlobal = XNew + Triangle.speed
  #  print("done right")
    return(XGlobal)


def Triangle_tile_up(YNew):
    global YGlobal
    YGlobal = YNew + Triangle.speed
   # print("done up")
    return(YGlobal)

def Triangle_tile_down(YNew):
    global YGlobal
    YGlobal = YNew - Triangle.speed
   # print("done down")
    return(YGlobal)
 
'''
Triangle_tile_right(70)
Triangle_tile_left(70)
Triangle_tile_up(70)
Triangle_tile_down(70)
'''
#print (Triangle_tile_left(XGlobal), YGlobal )
'''
Triangle_tile_left(XGlobal)
Triangle_tile_left(XGlobal)
Triangle_tile_left(XGlobal)
Triangle_tile_up(YGlobal) 
Triangle_tile_right(XGlobal)
print( XGlobal, YGlobal)
'''

def Collision_left():
    pass #the function detects if the x and y coordinates of the enemy 

def Collision_rignt():
    pass

def Collision_down():
    pass

def Collision_up():
    pass



while Collision_left == True:
    Triangle_tile_left(XGlobal)
    print(XGlobal)
    if Collision_left == False:
        break

'''
print (Triangle_tile_left( XGlobal  ) )
print (Triangle_tile_left( XGlobal  ) )  # repeated the code three times to test if the are consistant. 
print (Triangle_tile_left( XGlobal  ) )
