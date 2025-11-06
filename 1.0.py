class vehical:
    def __init__(self,color,initial_speed=0):
        self.color=color
        self.speed=initial_speed
    def accelarate(self,speed):
        self.speed+=speed
        print(f"the {self.color} car is driving at {self.speed}km")
    def __str__(self):
        return f'{self.color} car speed:{self.speed}km'


toyota=vehical(color="red")
mazda=vehical(color="blue")
print(toyota.color)
print(toyota.speed)
toyota.accelarate(10)
print(toyota.speed)
print(mazda.color)
print(mazda.speed)
mazda.accelarate(10)
print(mazda.speed)
mazda.accelarate(10)
print(toyota)
