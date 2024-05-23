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
        super().IncreaseSpeed()
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

#vehicle mr oz
"""

class Vehicle:
    def __init__(self, ID, MaxSpeed, IncreaseAmount):
        self._ID = ID  # Changed to protected
        self._MaxSpeed = MaxSpeed  # Changed to protected
        self._IncreaseAmount = IncreaseAmount  # Changed to protected
        self._CurrentSpeed = 0  # Changed to protected
        self._HorizontalPosition = 0  # Changed to protected

    def GetCurrentSpeed(self):
        return self._CurrentSpeed

    def GetIncreaseAmount(self):
        return self._IncreaseAmount

    def GetMaxSpeed(self):
        return self._MaxSpeed

    def GetHorizontalPosition(self):
        return self._HorizontalPosition

    def SetCurrentSpeed(self, CurrentSpeed):
        self._CurrentSpeed = CurrentSpeed
        if self._CurrentSpeed > self._MaxSpeed:
            self._CurrentSpeed = self._MaxSpeed
        self._HorizontalPosition += self._CurrentSpeed

    def IncreaseSpeed(self):
        self.SetCurrentSpeed(self._CurrentSpeed + self._IncreaseAmount)

    def OutputValues(self):
        print("Current position = ", self.GetHorizontalPosition())
        print("Current speed = ", self.GetCurrentSpeed())

class Helicopter(Vehicle):
    def __init__(self, ID, MaxSpeed, IncreaseAmount, VerticalChange, MaximumHeight):
        super().__init__(ID, MaxSpeed, IncreaseAmount)
        self._VerticalPosition = 0  # Changed to protected
        self._VerticalChange = VerticalChange  # Changed to protected
        self._MaximumHeight = MaximumHeight  # Changed to protected

    def IncreaseSpeed(self):
        self._VerticalPosition += self._VerticalChange
        if self._VerticalPosition > self._MaximumHeight:
            self._VerticalPosition = self._MaximumHeight
        super().IncreaseSpeed()

    def OutputValues(self):
        super().OutputValues()
        print("Vertical position = ", self._VerticalPosition)

# Example usage
Car = Vehicle("Tiger", 100, 20)
Heli = Helicopter("Lion", 350, 40, 3, 100)
Car.IncreaseSpeed()
Car.IncreaseSpeed()
Car.OutputValues()
Heli.IncreaseSpeed()
Heli.IncreaseSpeed()
Heli.OutputValues()
"""