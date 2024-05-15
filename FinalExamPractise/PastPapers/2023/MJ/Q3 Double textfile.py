
class Employee: 
    def __init__(self, EmpNum, Pay, Job): 
        self.__HourlyPay = Pay 
        self.__EmployeeNumber = EmpNum 
        self.__JobTitle = Job  
        self.__PayYear2022 = [0.00] * 52  # Initialize pay for each week to 0
        
    def GetEmployeeNumber(self): 
        return self.__EmployeeNumber
    
    def SetPay(self, WeekNumber, Hours): 
        self.__PayYear2022[WeekNumber-1] = Hours * self.__HourlyPay
        
    def GetTotalPay(self): 
        return sum(self.__PayYear2022)

class Manager(Employee): 
    def __init__(self, EmpNum, Pay, Job, Bonus): 
        super().__init__(EmpNum, Pay, Job) 
        self.__BonusValue = Bonus
    
    def SetPay(self, WeekNumber, Hours): 
        Hours = Hours * (1 + self.__BonusValue / 100) 
        super().SetPay(WeekNumber, Hours) 

# Initialize an empty list to store employee objects
Employees = []

try: 
    with open("Employees.txt", 'r') as File: 
        for _ in range(8): 
            Pay = float(File.readline()) 
            ID = File.readline().strip()  # Strip to remove newline character
            Temp = File.readline().strip()  # Strip to remove newline character
            try: 
                Bonus = float(Temp) 
                Title = File.readline().strip()  # Strip to remove newline character
                Employees.append(Manager(ID, Pay, Title, Bonus)) 
            except ValueError: 
                Title = Temp 
                Employees.append(Employee(ID, Pay, Title)) 
except IOError: 
    print("Could not find file") 

def EnterHours(): 
    try: 
        with open("HoursWeek1.txt", 'r') as File: 
            for _ in range(8): 
                EmpID = File.readline().strip()  # Strip to remove newline character
                for emp in Employees: 
                    if emp.GetEmployeeNumber() == EmpID: 
                        emp.SetPay(1, float(File.readline())) 
    except IOError: 
        print("Could not find file")

EnterHours() 

for emp in Employees: 
    print(emp.GetEmployeeNumber(), " ", emp.GetTotalPay())
'''
class SaleData:
    def __init__(self, SaleIDp, Quantityp):
        self.SaleID = SaleIDp  # string
        self.Quantity = Quantityp  # integer

CircularQueue = [SaleData("", -1) for _ in range(5)]  # SaleData, 5 items
NumberOfItems = 0  # int
Head = 0  # int
Tail = 0  # int

def Enqueue(RecordToAdd):
    global NumberOfItems, Head, Tail  # int
    if NumberOfItems == 5:
        return -1
    else:
        CircularQueue[Tail] = RecordToAdd
        Tail = (Tail + 1) % 5
        NumberOfItems += 1
        return 1

def Dequeue():
    global NumberOfItems, Head, Tail  # int
    RecordRemoved = SaleData("", -1)
    if NumberOfItems != 0:
        RecordRemoved = CircularQueue[Head]
        Head = (Head + 1) % 5
        NumberOfItems -= 1
    return RecordRemoved

def EnterRecord():
    ID = input("Enter ID: ")
    QuantityP = int(input("Enter quantity: "))  # Convert input to integer
    Record = SaleData(ID, QuantityP)
    if Enqueue(Record) == -1:
        print("Full")
    else:
        print("Stored")

EnterRecord()
EnterRecord()
EnterRecord()
EnterRecord()
EnterRecord()
EnterRecord()

ReturnValue = Dequeue()
if ReturnValue.SaleID == "":
    print("No items")
else:
    print(ReturnValue.SaleID, " ", ReturnValue.Quantity)

EnterRecord()

for record in CircularQueue:
    print(record.SaleID, " ", record.Quantity)

'''