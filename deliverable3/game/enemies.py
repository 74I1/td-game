





class enemy:
    def __init__(self,name,speed,attack, drop, health, sprite):   #the default framework for the enemy class with name, move speed, attack damage and drops
        self.name = name                          # enemies should also have sprite boxes which work withh the Collistion functions
        self.speed = speed
        self.attack = attack
        self.drop = drop
        self.health = health
        self.sprite = sprite
        
class Triangle(enemy):
    def move_speed(self):        # the enemy triangel with the structure of the enemy class with set name, speed, attack, and drop
        None
    def total_attack(self):
        None
    def total_drop(self):
        None
    def total_health(self):
        None


class Circle(enemy):
    def move_speed(self):
        None #5
    def total_attack(self):
        None #2
    def total_drop(self):
        None # 2
    def total_health(self):
        None #15

CircleImage = None   #placeholder images
TriangleImage = None


Circle = enemy(Circle, 5, 2, 2, 25, CircleImage)
print(Circle.name)
print(Circle.attack)
print(Circle.speed)
print(Circle.drop)
print(Circle.health)


Triangle = enemy(Triangle, 3, 2, 1, 15, TriangleImage)
print(Triangle.name)
print(Triangle.speed)
print(Triangle.attack)
print(Triangle.drop)
print(Triangle.health)



    
    