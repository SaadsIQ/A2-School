class Employee:
    def __init__(self,hourlyPay,employeeNumber,jobTitle):
        self.__HourlyPay = hourlyPay #REAL
        self.__EmployeeNumber = employeeNumber #STRING
        self.__Jobtitle = jobTitle #STRING
        self.__PayYear2022 = [0.00]*52 #Array 52 elements float
        
    def GetEmployeeNumber(self):
        return self.__EmployeeNumber
    
    def SetPay(self,weekNumber,hoursWorked):
        self.__PayYear2022[weekNumber-1]=hoursWorked * self.__HourlyPay

    def GetTotalPay(self):
        return sum(self.__PayYear2022)

class Manager(Employee):
    def __init__(self,hourlypay,employeeNumber,jobTitle,bonusValue):
        super().__init__(hourlyPay,employeeNumber,jobTitle)
        self.__BonusValue = bonusValue
    def SetPay(self, weekNumber, hoursWorked):
        hoursWorked = hoursWorked + ((self.__BonusValue/100)*hoursWorked)
        super().SetPay(weekNumber,hoursWorked)

EmployeeArray = [] #Array of type Employee 8 elements
Filename = "Employees.txt"
temp = ""
try:
    with open(Filename,"r") as File:
        for line in range(8):
            hourlyPay = float(File.readline())
            employeeNumber = File.readline().strip()
            temp = File.readline().strip()
            try: 
                bonus = float(temp)
                title = File.readline().strip()
                EmployeeArray.append(Manager(hourlyPay,employeeNumber,title,bonus))
            except ValueError:
                title = temp
                EmployeeArray.append(Employee(hourlyPay,employeeNumber,title))
    
except FileNotFoundError:
    print("file not found")

def EnterHours():
    Filename = "HoursWeek1.txt"
    try:
        with open(Filename,"r") as File:
            for _ in range(8):
                EmpID = File.readline().strip()
                for i in EmployeeArray:
                    if i.GetEmployeeNumber() == EmpID:
                        i.SetPay(1,float(File.readline()))
        File.close()
    except FileNotFoundError:
        print("File not found")

EnterHours()
for i in EmployeeArray:
    print(i.GetEmployeeNumber()," ",i.GetTotalPay())