class vehicle:
    def __init__ (self , maxspeed , milage ):
        self.maxspeed = maxspeed
        self.milage = milage 
modelX = vehicle( 240 , 18 )
print("Model Max Speed : ", modelX.maxspeed )
print("Model Max Milage : ", modelX.milage)