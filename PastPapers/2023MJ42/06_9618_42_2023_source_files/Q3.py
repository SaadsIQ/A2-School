class Employee:
    def __init__(self, HourlyPay, EmployeeNumber, JobTitle, PayYear2022):
        self.__HourlyPay = HourlyPay
        self.__EmployeeNumber = EmployeeNumber
        self.__Jobtitle = JobTitle
        self.__PayYear2022 = []
        for x in range(0,52):
            self.__PayYear2022[x] = 0.00
    def GetEmployeeNumber(self):
        return self.__EmployeeNumber
    def SetPay(self,weeknumber, hours):
        self.__PayYear2022[weeknumber-1] = hours * self.__HourlyPay
    def GetTotalPay(self):
        TotalPay = 0
        for x in range(0,52):
            TotalPay = self.__PayYear2022[x] + TotalPay
        return TotalPay
class Manager(Employee):
    def __init__(self, bonusValue, hourlyPay, employeeNumber, jobTitle):
        super().__init__(employeeNumber, hourlyPay, jobTitle)
        self.__bonusValue = bonusValue
    def SetPay(self, weeknumber, hoursWorked):
        pay = hoursWorked *(1+self.__bonusValue/100)
        super().SetPay(weeknumber, pay)

EmployeeArray = []
fileName = "Employees.txt"
try:
    
except FileNotFoundError:
    print("File not found")
