class vehical:
    def __init__(self,color,initial_speed=0):
        self.color=color
        self.speed=initial_speed
    def accelarate(self,speed):
        self.speed+=speed


toyota=vehical(color="red")
print(toyota.color)
print(toyota.speed)
toyota.accelarate(10)
print(toyota.speed)
