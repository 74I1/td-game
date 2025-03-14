
#speed = 5
#health = 10
#attack = 2
class enemy:
    def __init__(self,name,speed,attack, drop):   #the default framework for the enemy class with name, move speed, attack damage and drops
        self.name = name
        self.speed = speed
        self.attack = attack
        self.drop = drop
class Blocks:
    def __init__(self,name,health,cost):      # the default framework for the placibles class with name, health, abd cost
        self.name = name
        self.health = health
        self.cost = cost

class Triangle(enemy):
    def move_speed(self):        # the enemy triangel with the structure of the enemy class with set name, speed, attack, and drop
        speed += 9
   # def total_health(self):
    #    health += 0
    def total_attack(self):
        attack += 3
    def total_drop(self):
        drop += 3
        
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

Triangle = enemy(Triangle, 9, 3, 3)
print(Triangle.name)
print(Triangle.speed)
print(Triangle.attack)
print(Triangle.drop)
        
Square = Blocks(Square, 20, 5)
print(Square.name)
print(Square.cost)
print(Square.health)        