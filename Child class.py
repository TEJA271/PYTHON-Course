class DAD:
    def __init__(  self  ,  eyes  ,  aggresive  ):
        self.eyes = eyes
        self.aggresive = aggresive

    def display(self):
        print(" Your Eyes Are ",self.eyes)
        print(" Your Aggresive is ",self.aggresive)

class son(DAD):
    def __init__(  self  ,  name  ,  age  ,  eyes  ,  aggresive  ):
        self.name = name 
        self.age = age

        DAD.__init__(  self  ,  eyes  ,  aggresive  )

object = son( "LION" ,  8  ," Yellow ",True)

object.display()