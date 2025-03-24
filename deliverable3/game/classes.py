

#speed = 5
#health = 10
#attack = 2
import time
#import pygame
#screen = pygame.display.set_mode((1280, 720))

    
class Blocks:
    def __init__(self,name,health, cost, sprite, attack, range ):      # the default framework for the placibles class with name, health, abd cost
        self.name = name
        self.health = health
        self.cost = cost
        self.sprite = sprite
        self.attack = attack
        self.range = range  
   
   
class Square(Blocks):
    def total_health(self):
        None#20
    def total_cost(self):
        None #5
    def total_attack(self):
        None # 3
    def EnemyInRange(self):
        while None == True:   #None is a placeholder of a hypothetical colision detection vairable which returns true when the enemy is touching the Rectangle's range sprite
          pass



class Rectangle(Blocks):
    def total_health(self):
        None #50
    def total_cost(self):
        None #25
    def Total_attack(self):
        None #5
    def EnemyInRange(self):
        while None == True:
          pass



RectangleImage = None #placeholder for potential unit display sprites
SquareImage = None

RectangleRange = None #placeholder for ptotential range sprites
SquareRange = None

Rectangle = Blocks(Rectangle, 50, 25, RectangleImage, 5, RectangleRange)  # testing the placible Rectangel, prints the health, cost, and name for the stats for Rectangel
print(Rectangle.cost)
print(Rectangle.health)
print(Rectangle.name)
print(Rectangle.attack)
      
Square = Blocks(Square, 20, 5, SquareImage, 3, SquareRange)
print(Square.name)
print(Square.health)
print(Square.cost)        
print(Square.attack)

