class Employee:
    def __init__(self,hourlyPay,employeeNumber,jobTitle):
        self.__HourlyPay = hourlyPay #REAL
        self.__EmployeeNumber : employeeNumber #STRING
        self.__Jobtitle = jobTitle #STRING
        self.__PayYear2022 = [] #Array 52 elements float
        for _ in range(0,52):
            self.__PayYear2022[_] = 0.0
    def GetEmployeeNumber(self):
        return self.__EmployeeNumber
    def SetPay(self,weekNumber,hoursWorked):
        payForWeek = self.__HourlyPay * hoursWorked
        self.__PayYear2022[weekNumber] = payForWeek
    def GetTotalPay(self):
        total = 0
        for index in range(0,52):
            total = total + self.__PayYear2022[index]
        return total

class Manager(Employee):
    def __init__(self,bonusValue,hourlyPay,employeeNumber,jobTitle):
        super().__init__(employeeNumber,hourlyPay,jobTitle)
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
            employeeNumber = int(File.readline().strip())
            temp = File.readline().strip()
            try: 
                bonus = float(temp)
                title = File.readline().strip()
                EmployeeArray.append(Manager(hourlyPay,employeeNumber,title,bonus))
            except:
                title = temp
                EmployeeArray.append(Employee(hourlyPay,employeeNumber,title))
    File.close()
except FileNotFoundError:
    print("file not found")

def EnterHours():
    Filename = "HoursWeek1.txt"
    try:
        with open(Filename,"r") as File:
            for line in File:
                EmployeeNumber = int(File.readline())
                hoursworked = float(File.readline().strip())
                for i in range(0,8):
                    if Employee[i].GetEmployeeNumber() == EmployeeNumber:
                        Employee[i].SetPay(1,hoursworked)
        File.Close()
    except FileNotFoundError:
        print("File not found")

EnterHours()
for i in range(0,8):
    print("Employee number: ",Employee[i].GetEmployeeNumber(),"Employee pay",Employee[i].GetTotalPay())