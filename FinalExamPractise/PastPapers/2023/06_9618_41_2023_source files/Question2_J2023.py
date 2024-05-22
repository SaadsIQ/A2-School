class Vehicle:
    def __init__(self,ID,MaxSpeed,IncreaseAmmount):
        self.__ID = ID #STRING
        self.__MaxSpeed = MaxSpeed #INTEGER
        self.__IncreaseAmmount = IncreaseAmmount #INTEGER
        self.__CurrentSpeed = 0 #INTEGER
        self.__HorizontalPosition = 0 #INTEGER
    def GetCurrentSpeed(self):
        return self.__CurrentSpeed
    def GetIncreaseAmmount(self):
        return self.__IncreaseAmmount
    def GetMaxSpeed(self):
        return self.__MaxSpeed
    def GetHorizontalPosition(self):
        return self.__HorizontalPosition
    def SetCurrentSpeed(self,CurrentSpeed):
        self.__CurrentSpeed = CurrentSpeed
    def SetHorizontalPosition(self,HorizontalPosition):
        self.__HorizontalPosition = HorizontalPosition
    
    def IncreaseSpeed(self):
        self.__CurrentSpeed = self.__CurrentSpeed +self.__IncreaseAmmount
        if self.__CurrentSpeed > self.__MaxSpeed:
            self.__CurrentSpeed = self.__MaxSpeed
        self.__HorizontalPosition = self.__HorizontalPosition + self.__CurrentSpeed
    def OutputValues(self):
        print("Current position = ", Vehicle.GetHorizontalPosition(self))
        print("Current speed = ", Vehicle.GetCurrentSpeed(self))
        

class Helicopter(Vehicle):
    def __init__(self,ID,Maxspeed,IncreaseAmmount,VerticalChange,MaximumHeight):
        super().__init__(ID,Maxspeed,IncreaseAmmount)
        self.__VerticalPositon = 0 #INTEGER
        self.__VerticalChange = VerticalChange #INTEGER
        self.__MaximumHeight = MaximumHeight #INTEGER
    def IncreaseSpeed(self):
        self.__VerticalPositon = self.__VerticalPositon + self.__VerticalChange
        if self.__VerticalPositon > self.__MaximumHeight:
            self.__VerticalPositon = self.__MaximumHeight
        super().SetCurrentSpeed(self,Vehicle.GetCurrentSpeed(self) + Vehicle.GetIncreaseAmmount(self))
        if Vehicle.GetCurrentSpeed(self) > Vehicle.GetMaxSpeed(self):
            Vehicle.SetCurrentSpeed(self,Vehicle.GetMaxSpeed(self))
    def OutputValues(self):
        print("Current position = ", Vehicle.GetHorizontalPosition(self))
        print("Current speed = ", Vehicle.GetCurrentSpeed(self))
        print("Vertical position = ",self.__VerticalPositon)

Car = Vehicle("Tiger",100,20)
Heli = Helicopter("Lion",350,40,3,100)
Car.IncreaseSpeed()
Car.IncreaseSpeed()
Car.OutputValues()
Heli.IncreaseSpeed()
Heli.IncreaseSpeed()
Heli.OutputValues()