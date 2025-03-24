import sys

XGlobal = 30
YGlobal = 30


class path:
    def __init__(self, sprite, direction):    #sprite-  is the apperance of the path entity,  direction- decides the path's direction for enemy movement
        self.direction = direction
        self.sprite = sprite


class Up(path):
    def collision():
        None                # adds collision checks and detects if the enemy sprite is in contact with the "up path" sprite, returns True when they are touching.
    def Triangle_tile_up(YNew):
        global YGlobal
        YGlobal = YNew + Triangle.speed
   # print("done up")
        return(YGlobal)       # also make it so that if the enemy sprite isn't in contact with any path sprites it will continuously move in the direction of the last path sprite it made contact until a new path sprite is present
                            # probably use the 'if' and 'elif' statements 


class Down(path):
    def collision():
        None
    def Triangle_tile_down(YNew):
        global YGlobal
        YGlobal = YNew - Triangle.speed
   # print("done down")
        return(YGlobal)


class Left(path):
    def collision():
        None
    def Triangle_tile_left( XNew ):
        global XGlobal
        XGlobal = XNew - Triangle.speed        # Triangle.speed represents the enemy speed attribute    XGlobal represents the intital position        XNew represents the new position after the affect of the movement tiles
   # print("done left")               
        return(XGlobal)            

class Right(path):
    def collision():
        None
    def Triangle_tile_right(XNew):
        global XGlobal
        XGlobal = XNew + Triangle.speed
  #  print("done right")
        return(XGlobal)    


 
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
'''