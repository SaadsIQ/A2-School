# 1D BubbleSort

def bubblesort(arr):
  n= len(arr)
  for i in range (n):
    for j in range (0,n-i-1):
      if arr[j]>arr[j+1]:
        arr[j],arr[j+1]=arr[j+1],arr[j]
arr=[100,20,15,1,4,67,7,9,45,3]
bubblesort(arr)
print(" ".join(map(str, arr)))

# 2D BubbleSort
import random

def Printarray(ArrayData):
    for row in ArrayData:
        print(" ".join(map(str, row)))

ArrayData = [[0]*10 for _ in range(10)]  # integer
for x in range(10):
    for y in range(10):
        ArrayData[x][y] = random.randint(1, 100)

print("Before")
Printarray(ArrayData)

ArrayLength = 10
for X in range(ArrayLength):
    for Z in range(ArrayLength - 1):
        for Y in range(ArrayLength - Z - 1):
            if ArrayData[X][Y] > ArrayData[X][Y+1]:
                ArrayData[X][Y], ArrayData[X][Y+1] = ArrayData[X][Y+1], ArrayData[X][Y]

print("After")
Printarray(ArrayData)

# Binary search
def BinarySearch(SearchArray, Lower, Upper, SearchValue):
  if Upper >= Lower:
      Mid = Lower + (Upper - Lower) // 2
      if SearchArray[0][Mid] == SearchValue:
          return Mid
      elif SearchArray[0][Mid] > SearchValue:
          return BinarySearch(SearchArray, Lower, Mid - 1, SearchValue)
      else:
          return BinarySearch(SearchArray, Mid + 1, Upper, SearchValue)
  else:
      return -1
SearchValue = int(input("Enter the number you want to search: "))
print(BinarySearch(ArrayData, 0, ArrayLength - 1, SearchValue))

# Insertion sort
Jobs = [[0 for _ in range(2)] for _ in range(100)]
NumberOfJobs = 0
def Initialise():
 global Jobs 
 global NumberOfJobs 
 for x in range(0, 100):
    Jobs.append([-1,-1])
    NumberOfJobs = 0
def AddJob(JobNumber, Priority):
 global NumberOfJobs
 global Jobs
 if NumberOfJobs == 100:
    print("Not added")
 else:
    Jobs[NumberOfJobs] = [JobNumber, Priority]
    print("Added")
    NumberOfJobs = NumberOfJobs + 1

def InsertionSort():
  global Jobs
  global NumberOfJobs
  for I in range(1, NumberOfJobs):
      Current1 = Jobs[I][0]
      Current2 = Jobs[I][1]
      while I > 0 and Jobs[I-1][1] > Current2:
          Jobs[I][0] = Jobs[I-1][0]
          Jobs[I][1] = Jobs[I-1][1]
          I = I - 1
      Jobs[I][0] = Current1
      Jobs[I][1] = Current2
def PrintArray():
 global Jobs
 global NumberOfJobs
 for X in range(0, NumberOfJobs):
     print(str(Jobs[X][0]), " priority ", str(Jobs[X][1]))


Initialise()
AddJob(12,10)
AddJob(526,9)
AddJob(33,8)
AddJob(12,9)
AddJob(78,1)
AddJob(122,0.1)
InsertionSort()
PrintArray()


# Stack
StackData = [0] * 10
StackPointer = 0

def PrintArray():
    global StackData
    global StackPointer
    print(StackPointer)
    for x in range(0, 10):
        print(StackData[x])

def Push(DataToPush):
    global StackData
    global StackPointer
    if StackPointer == 10:
        return False
    else:
        StackData[StackPointer] = DataToPush
        StackPointer += 1
        return True

def Pop():
    global StackData
    global StackPointer
    if StackPointer == 0:
        print("Stack is empty")
        return None
    else:
        ReturnData = StackData[StackPointer - 1]
        StackData[StackPointer - 1] = None  # Set the popped item to None
        StackPointer -= 1
        return ReturnData

# Push 11 numbers
for _ in range(0, 11):
    TempNumber = input("Enter a number: ")
   
    if Push(TempNumber):
        print("Stored")
    else:
        print("Stack full")

PrintArray()

# Ask how many pops are needed
num_pops = int(input("How many elements do you want to pop? "))
for _ in range(num_pops):
    popped = Pop()
    if popped is not None:
        print("Popped:", popped)
    else:
        break

PrintArray()


#Queue
Queue = [-1] * 20
HeadPointer = -1
TailPointer = 0

def Enqueue(Data):
    global TailPointer
    global HeadPointer
    if HeadPointer == -1:
        HeadPointer = 0
    if TailPointer < len(Queue):
        try:
            num = int(Data)
            Queue[TailPointer] = num
            TailPointer += 1
            return True
        except ValueError:
            return False
    return False

def RecursiveOutput(Start):
    if Start == 0:
        return Queue[Start]
    return Queue[Start] + RecursiveOutput(Start - 1)

num_to_input = min(int(input("How many numbers do you want to input (up to 20)? ")), 20)

for _ in range(num_to_input):
    while True:
        num = input("Enter a number to enqueue: ")
        if Enqueue(num):
            break
        print("Invalid input. Please enter a valid number.")

print("Enqueued numbers:", *Queue[:TailPointer])
print("Sum of enqueued numbers:", RecursiveOutput(TailPointer - 1))

class SaleData: 
 def __init__(self, SaleIDp, Quantityp): 
    self.SaleID = SaleIDp #string 
    self.Quantity = Quantityp #integer
  
CircularQueue = [] #SaleData, 5 items 
global NumberOfItems #int 
global Head #int 
global Tail #int 

def Enqueue(RecordToAdd): 
   global NumberOfItems #int 
   global Head #int 
   global Tail #int 
   if(NumberOfItems == 5): 
      return -1 
   else: 
        CircularQueue[Tail] = RecordToAdd 
        if(Tail == 4): 
            Tail = 0 
        else: 
           Tail +=1 
           NumberOfItems +=1 
           return 1

def Dequeue(): 
    global NumberOfItems #int 
    global Head #int 
    global Tail #int 
    RecordRemoved = SaleData("", -1) 
    if NumberOfItems != 0: 
       RecordRemoved = CircularQueue[Head] 
       NumberOfItems -=1 
       if Head == 4: 
          Head = 0 
       else: 
          Head +=1 
    return RecordRemoved
def EnterRecord(): 
  ID = input("Enter ID") 
  QuantityP = input("Enter quantity") 
  Record = SaleData(ID, QuantityP) 
  if Enqueue(Record) == -1: 
      print("Full") 
  else: 
      print("Stored")

NumberOfItems = 0 
Head = 0 
Tail = 0 
for x in range(0, 5): 
    CircularQueue.append((SaleData("",-1)))



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
for x in range(0, 5): 
 print(CircularQueue[x].SaleID, " ", CircularQueue[x].Quantity)


class TreasureChest:

    def __init__(self, question: str, answer: int, points: int):
        self.question = question
        self.answer = answer
        self.points = points

    def check_answer(self, guess: int) -> bool:
        return self.answer == guess

    def get_points(self, attempts: int) -> int:
        if attempts == 1:
            return self.points
        elif attempts == 2:
            return self.points // 2
        elif attempts <= 4:
            return self.points // 4
        return 0

ArrayTreasure = []
def read_data(filename: str):
    with open(filename, "r") as file:
        while True:
            question = file.readline().strip()
            if not question:
                break
            answer = int(file.readline().strip())
            points = int(file.readline().strip())
            ArrayTreasure.append(TreasureChest(question, answer, points))

read_data("treasureChestData.txt")
choice = int(input("Pick a treasure chest to open (1-5): "))
chest = ArrayTreasure[choice - 1]
attempts = 0
correct = False
while not correct:
    guess = int(input(f"{chest.question}: "))  
    correct = chest.check_answer(guess)
    attempts += 1
print("Correct! Points earned:", chest.get_points(attempts))

class Employee:

    def __init__(self, emp_num, pay, job):
        self.employee_number = emp_num
        self.hourly_pay = pay
        self.job_title = job
        self.pay_year_2022 = [0.0] * 52

    def get_employee_number(self):
        return self.employee_number

    def set_pay(self, week_number, hours):
        if 1 <= week_number <= 52:
            self.pay_year_2022[week_number - 1] = hours * self.hourly_pay

    def get_total_pay(self):
        return sum(self.pay_year_2022)


class Manager(Employee):

    def __init__(self, emp_num, pay, job, bonus):
        super().__init__(emp_num, pay, job)
        self.bonus_value = bonus

    def set_pay(self, week_number, hours):
        super().set_pay(week_number, hours * (1 + self.bonus_value / 100))


def read_employees(filename, employee_list):
    with open(filename, "r") as file:
        while (line := file.readline().strip()):
            pay = float(line)
            emp_num = file.readline().strip()
            job_or_bonus = file.readline().strip()
            try:
                bonus = float(job_or_bonus)
                job = file.readline().strip()
                employee_list.append(Manager(emp_num, pay, job, bonus))
            except ValueError:
                employee_list.append(Employee(emp_num, pay, job_or_bonus))


def enter_hours(filename, employee_list):
    with open(filename, "r") as file:
        while (emp_num := file.readline().strip()):
            hours = float(file.readline().strip())
            employee = next(
                (e
                 for e in employee_list if e.get_employee_number() == emp_num),
                None,
            )
            if employee:
                employee.set_pay(1, hours)
employee_list = []

read_employees("Employees.txt", employee_list)
enter_hours("HoursWeek1.txt", employee_list)

for employee in employee_list:
    print(f"{employee.get_employee_number()} {employee.get_total_pay()}")

#Binary tree
ArrayNodes = []
for x in range(0, 20):
    ArrayNodes.append([-1, -1, -1])
ArrayNodes = [[1,20,5],[2,15,-1],[-1,3,3],[-1,9,4],[-1,10,-1],[-1,58,-1]]
FreeNodes = 6
RootPointer = 0

def SearchValue(Root, ValueToFind):
    global ArrayNodes
    if Root == -1:
         return -1
    elif ArrayNodes[Root][1] == ValueToFind:
        return Root
    elif ArrayNodes[Root][1] == -1:
        return -1
    if(ArrayNodes[Root][1] > ValueToFind):
        return SearchValue(ArrayNodes[Root][0], ValueToFind)
    if(ArrayNodes[Root][1] < ValueToFind):
        return SearchValue(ArrayNodes[Root][2], ValueToFind)

def PostOrder(RootNode):
    if RootNode[0] != -1:
        PostOrder(ArrayNodes[RootNode[0]]) 
    if RootNode[2] != -1:
        PostOrder(ArrayNodes[RootNode[2]])
    print(str(RootNode[1]))

ReturnValue = SearchValue(RootPointer, 15)
if ReturnValue == -1:
    print("Not found")
else:
    print("Found at " + str(ReturnValue))

PostOrder(ArrayNodes[RootPointer])

class Card:
    #Number as integer
    #Colour as string
    def __init__(self, Number1, Colour1):
        self.__Number = Number1
        self.__Colour = Colour1
    def GetNumber(self):
        return self.__Number
    def GetColour(self):
         return self.__Colour
OneRed = Card(1, "red")
TwoRed = Card(2, "red")
ThreeRed = Card(3, "red")
FourRed = Card(4, "red")
FiveRed = Card(5, "red")
OneBlue = Card(1, "blue")
TwoBlue = Card(2, "blue")
ThreeBlue = Card(3, "blue")
FourBlue = Card(4, "blue")
FiveBlue = Card(5, "blue")
OneYellow = Card(1, "yellow")
TwoYellow = Card(2, "yellow")
ThreeYellow = Card(3, "yellow")
FourYellow = Card(4, "yellow")
FiveYellow = Card(5, "yellow")
# alternative

OneRed, TwoRed, ThreeRed, FourRed, FiveRed = [Card(i, "red") for i in range(1, 6)]
OneBlue, TwoBlue, ThreeBlue, FourBlue, FiveBlue = [Card(i, "blue") for i in range(1, 6)]
OneYellow, TwoYellow, ThreeYellow, FourYellow, FiveYellow = [Card(i, "yellow") for i in range(1, 6)]


class Hand:
 #Cards[10] as Card
 #FirstCard as integer
 #NumberCards as integer

    def __init__(self, Card1, Card2, Card3, Card4,Card5):
        self.__Cards = []
        self.__Cards.append(Card1)
        self.__Cards.append(Card2)
        self.__Cards.append(Card3)
        self.__Cards.append(Card4)
        self.__Cards.append(Card5)
        self.__FirstCard = 0
        self.__NumberCards = 5
    def GetCard(self, Position):
        return self.__Cards[Position]
Player1 = Hand(OneRed, TwoRed, ThreeRed, FourRed, 
OneYellow)
Player2 = Hand(TwoYellow, ThreeYellow, FourYellow, 
FiveYellow, OneBlue)
def CalculateValue(Player):
    Score = 0
    for Count in range(0, 4):
        CardGot = Player.GetCard(Count)
        Score = Score + CardGot.GetNumber()
        Colour = CardGot.GetColour()
        if Colour == "red":
            Score = Score + 5
        elif Colour == "blue":
            Score = Score + 10
        else:
            Score = Score + 15
    return Score
Player1score = CalculateValue(Player1)
Player2score = CalculateValue(Player2)
if Player1score > Player2score:
     print("Player 1 wins")
elif Player1score < Player2score:
     print("Player 2 wins")
else:
     print("It's a draw")

class Card:
    def __init__(self, number, colour):
        self.number = number
        self.colour = colour

class Hand:
    def __init__(self, *cards):
        self.cards = list(cards)

def calculate_value(player):
    score = sum(card.number + (5 if card.colour == "red" else 10 if card.colour == "blue" else 15)
                for card in player.cards)
    return score
# Initialize cards
cards = [Card(number, colour) for colour in ["red", "blue", "yellow"] for number in range(1, 6)]
# Initialize hands
Player1 = Hand(*cards[:5])
Player2 = Hand(*cards[5:])

Player1score = calculate_value(Player1)
Player2score = calculate_value(Player2)

if Player1score > Player2score:
     print("Player 1 wins")
elif Player1score < Player2score:
     print("Player 2 wins")
else:
     print("It's a draw")

DataArray = [0] * 100


def ReadFile():
    global DataArray
    try:
        TextFile = "IntegerData.txt"
        with open(TextFile, 'r') as File:
            for X in range(100):
                DataArray[X] = int(File.readline().rstrip('\n'))
    except IOError:
        print("Could not find file")


def FindValues():
    global DataArray
    DataToFind = -1

    while DataToFind < 1 or DataToFind > 100:
        DataToFind = int(input("Enter a number between 1 and 100: "))
        Total = 0
        for X in range(100):
            if DataArray[X] == DataToFind:
                Total += 1
    return Total

def BubbleSort():
    global DataArray
    N = 100
    for I in range(N-1):
        for J in range(N-I-1):
            if DataArray[J] > DataArray[J+1]:
                DataArray[J], DataArray[J+1] = DataArray[J+1], DataArray[J]

ReadFile()
print("The number appears " + str(FindValues()) + " times")
BubbleSort()
print(DataArray)




#Saad code




# Stack
stack = [None for i in range(0,int(input("Enter stack size: ")))]
# Initialize top and base pointers, and stackFull variable
topPointer = -1 # Top pointer set to -1 to signify stack is empty
basePointer = 0
stackFull = len(stack)
item = None

def push():
    global stack, topPointer, basePointer, stackFull
    if topPointer < stackFull-1:
        # Check if stack has space
        topPointer += 1
        # Increment top pointer so it points to first index in array
        item = int(input("Enter the item: "))
        stack[topPointer] = item
        # Assign the item to the array index at topPointer
        print("item pushed to stack", item)
    else:
        print("Stack full cannot push")

def pop():
    global stack,topPointer,basePointer, stackFull
    if topPointer >= basePointer:
        # Check if there are items in the stack
        stack[topPointer] = None
        topPointer = topPointer-1
        print("Popped item: ", item)
    else:
        print("Stack is empty")

def printmethod():
    global stack
    for index in range (0,stackFull):
        print(stack[index])

numPush = int(input("Enter how many items to push to stack: "))
for _ in range(numPush):
    push()
printmethod()
numPop = int(input("Enter how many items to pop from stack: "))
for _ in range(numPop):
    pop()
printmethod()

# Stack OOP
class Stack:
    def __init__(self):
        self.stack = []
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack) == 0:
            print("Stack empty")
        else:
            self.stack.pop(len(self.stack)-1)
    def printStack(self):
        print(self.stack)

stack = Stack()
stack.printStack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.printStack()
stack.pop()
stack.printStack()


# Queue
queue = [None for _ in range(0,int(input("Enter queue size: ")))]
print(queue)
frontPointer = 0
rearPointer = -1 # Set to -1 to indicate empty queue
queuesize = len(queue)
queueLength = 0
item = None

def enqueue():
    global queue,frontPointer,rearPointer,queuesize,queueLength
    if queueLength == queuesize:
        print("Queue full cannot enqeue")
    else:
        queueLength += 1
        rearPointer += 1
        item = int(input("Enter a item: "))
        queue[rearPointer] = item # Item added to position of the rear pointer// back of queue
        print("Item enqueued: ", item)
def dequeue():
    global queue,frontPointer,rearPointer,queuesize,queueLength
    if queueLength == 0:
       print("Queue empty cannot dequeue")
    else:
        item = queue[frontPointer] # Item set to the item stored at front of queue
        queue[frontPointer] = None # Front of queue set to None
        frontPointer += 1 # Front pointer incremented to point to next item 
        queueLength -= 1 # Queue length decremented to show a item has been removed
        queue[:] = queue[frontPointer:] # Items from the index of frontpointer and onwards are moved to the beginning of the queue
        frontPointer = 0 # frontPointer reset as after moving the data to the beginning of the queue the next item to be dequeued will be at index 0
        print("Item dequeued: ",item)

numEnqueue = int(input("Enter the number of items to enqueue: "))
for _ in range(0,numEnqueue):
    enqueue()
print(queue)
numDequeue = int(input("Enter the number of items to Dequeue: "))
for _ in range(0,numDequeue):
    dequeue()
print(queue)

# Queue OOP
class Queue:
    def __init__(self):
        self.queue = []
    def printQueue(self):
        print(self.queue)
    def Enqueue(self,value):
        self.queue.append(value)
    def Dequeue(self):
        if len(self.queue) <1:
            print("Queue is empty")
        else:

            return self.queue.pop(0)
        
queue = Queue()
queue.printQueue()
queue.Enqueue(1)
queue.Enqueue(2)
queue.Enqueue(3)
queue.printQueue()
queue.Dequeue()
queue.printQueue()

# Circular Queue
queue = [None for _ in range (0,int(input("Enter queue size: ")))]
frontPointer = -1
rearPointer = -1
queueSize = 0
queueMax = len(queue)
item = None

def Enqueue():
    global queue, frontPointer,rearPointer,queueSize,queueMax,item
    if queueSize == queueMax:
        print("Queue full cannot enqueue")
    else:
        if rearPointer == queueMax - 1:
            rearPointer = 0
        else:
            rearPointer += 1
        if frontPointer == -1:
            frontPointer = 0
        queueSize = queueSize + 1
        item = int(input("Enter a number: "))
        queue[rearPointer] = item
def Dequeue():
    global queue, frontPointer,rearPointer,queueSize,queueMax,item
    if queueSize == 0:
        print("Queue empty cannot dequeue")
    else:
        item = queue[frontPointer]
        queue[frontPointer] = None
        frontPointer += 1
        queueSize -= 1
        print("Item dequeued: ", item)
def printQueue():
    print(queue)

printQueue()
numEnqueue = int(input("How many items to enqueue: "))
for _ in range(0,numEnqueue):
    Enqueue()
printQueue()
numdDequeue = int(input("How many items to dequeue: "))
for _ in range(0,numEnqueue):
    Dequeue()
printQueue()

# Bubble sort
intArray = [5,24,12,64,78,99,10,53]

def bubbleSort(intArray):
    arrayLength = len(intArray)
    for i in range(arrayLength-1):
        for j in range(arrayLength-i-1):
            if intArray[j]> intArray[j+1]:
                intArray[j],intArray[j+1] = intArray[j+1], intArray[j]
    print(intArray)
bubbleSort(intArray)

# insertion sort
intArray = [100,1,20,5,7]
def insertionSort(intArray):
    arrayLength = len(intArray)
    # Iterate through the array starting from the second element
    for i in range(1,arrayLength):
        temp = intArray[i] # Store the current element in temp
        j = i -1 # Initialize j to the index of the last element in the sorted subarray
        while j>=0 and intArray[j]>temp:  # Move elements of the sorted subarray that are greater than temp to one position ahead
            intArray[j+1] = intArray[j] # Shift element to the right
            j -=1 # Move to the previous element
        intArray[j+1] = temp  # Insert the temp element into its correct position
    print(intArray)
insertionSort(intArray)

# linear search
intArray = [1,2,5,7,4,8,3]

def linearSearch(intArray):
    searchItem = int(input("Enter the item to search for: "))
    arrLength = len(intArray)
    counter = 0
    while counter != arrLength:
        if intArray[counter] == searchItem:
            print("Found",counter)
            break
        else:
            counter += 1
        if counter == arrLength:
            print("Not in list")
linearSearch(intArray)

# binary search
intArray = [1,2,3,4,5,6,7,8,9,10]
toFind = int(input("Enter the item to find: "))
found = False
start = 0 
end = len(intArray) - 1

while start <= end and found == False:
    mid = (start+end)//2
    if intArray[mid] == toFind:
        found = True
    else:
        if intArray[mid] < toFind:
            start = mid + 1
        else:
            end = mid -1
if found == True:
    print("Item found at index:", mid)
else:
    print("Item not in list")

# Treasure paper

# linked list
class node:
    def __init__(self, theData, nextNode):
        self.data = theData
        self.next = nextNode

class LinkedList:
    def __init__(self):
        self.linkedList = [node(1,1), node(5,4), node(6,7), node(7,-1), node(2,2), node(0,6), node(0,8), node(56,3), node(0,9), node(0,-1)]
        self.startPointer = 0
        self.emptyList = 5
            
    def output_nodes(self):
        currentPointer = self.startPointer
        while currentPointer != -1:
            print(str(self.linkedList[currentPointer].data))
            currentPointer = self.linkedList[currentPointer].next
                
    def addNode(self):
        dataToAdd = input("Enter the data to add: ")
        if self.emptyList <0 and self.emptyList > 9:
            return False
        else:
            newNode = node(int(dataToAdd), -1)
            self.linkedList[self.emptyList] = newNode
            previousPointer = 0
            currentPointer = self.startPointer
            while currentPointer!= -1:
                previousPointer = currentPointer
                currentPointer = self.linkedList[currentPointer].next
            self.linkedList[previousPointer].next = self.emptyList
            self.emptyList = self.linkedList[self.emptyList].next
        return True
myLinkedList = LinkedList()
myLinkedList.output_nodes()
myLinkedList.addNode()
myLinkedList.output_nodes()

# Treasure chest
class TreasureChest:
    def __init__(self, question, answer, points):
        self.question = question  # string
        self.answer = int(answer)  # integer
        self.points = int(points)  # integer

    def getQuestion(self):
        return self.question

    def checkAnswer(self, userAnswer):
        return userAnswer == self.answer

    def getPoints(self, attempts):
        if attempts == 1:
            return self.points
        elif attempts == 2:
            return int(self.points / 2)
        elif attempts == 3 or attempts == 4:
            return int(self.points / 4)
        else:
            return 0

def readData():
    FileName = "TreasureChestData.txt"
    arrayTreasure = []
    try:
        with open(FileName, "r") as File:
            for line in File:
                question = line.strip()
                answer = File.readline().strip()
                points = File.readline().strip()
                arrayTreasure.append(TreasureChest(question, answer, points))
    except FileNotFoundError:
        print("File Not Found")
    return arrayTreasure

def main():
    arrayTreasure = readData()
    if arrayTreasure:
        qExists = False
        Attempts = 1
        AnswerCheck = False
        while not qExists:
            qNum = int(input("Enter the question number: "))
            if 1 <= qNum <= 5:
                qExists = True
                while not AnswerCheck:
                    print(arrayTreasure[qNum - 1].getQuestion())
                    userAnswer = int(input("Enter your answer: "))
                    Correct = arrayTreasure[qNum - 1].checkAnswer(userAnswer)
                    if Correct:
                        AnswerCheck = True
                        Point = arrayTreasure[qNum - 1].getPoints(Attempts)
                        print("You got this many points:", Point)
                    else:
                        Attempts += 1


if __name__ == "__main__":
    main()

# Pictures paper
# iterative and recursive
def Unknown(x,y):
    if x < y:
        print(x+y)
        return Unknown(x+1,y)*2
    elif x == y:
        return 1
    else:
        print(x+y)
        return int(Unknown(x-1,y)/2)

"""
print("10 and 15") 
print(str(Unknown(10, 15))) 
print("10 and 10") 
print(str(Unknown(10, 10))) 
print("15 and 10") 
print(str(Unknown(15, 10)))
"""


def iterativeUnknown(x,y):
    total = 1
    while x != y:
        print(str(x + y))
        if x < y:
            x = x+1
            total = total * 2
        else:
            x = x-1
            total = int(total/2)
    return total
print("10 and 15") 
print(str(iterativeUnknown(10, 15))) 
print("10 and 10") 
print(str(iterativeUnknown(10, 10))) 
print("15 and 10") 
print(str(iterativeUnknown(15, 10)))

# picture
class Picture:
    def __init__(self, Description, Width, Height, FrameColour):
        self.__Description = Description #STRING
        self.__Width = Width #INTEGER
        self.__Height = Height #INTEGER
        self.__FrameColour = FrameColour #STRING
    
    def GetDescription(self):
        return self.__Description
    def GetWidth(self):
        return self.__Width
    def GetHeight(self):
        return self.__Height
    def GetColour(self):
        return self.__FrameColour

    def SetDescription(self, Description):
        self.__Description = Description

def readData(PictureArray):
    fileName = "Pictures.txt"
    counter = 0
    try:
        with open(fileName,"r") as File:
            for line in File:
                Description = line.strip().lower()
                Width = int(File.readline().strip())
                Height = int(File.readline().strip())
                FrameColour = File.readline().strip().lower()
                PictureArray[counter] = Picture(Description,Width,Height,FrameColour)
                counter = counter+1
    except FileNotFoundError:
            print("File not found")
    return counter, PictureArray

def printArray():
    index1 = 0
    for _ in range(NumberPicturesInArray):
        print(PictureArray[index1].GetColour(),PictureArray[index1].GetWidth(),PictureArray[index1].GetHeight(),PictureArray[index1].GetDescription())
        index1 += 1

PictureArray = [Picture("",0,0,"") for x in range(0,100)]

NumberPicturesInArray, PictureArray = readData(PictureArray)

print(NumberPicturesInArray)
printArray()

usercolour = str(input("Enter a color to search for: ")).lower()
userWidth = int(input("Enter the maximum width: "))
userHeight = int(input("Enter the maximum height: "))

for x in range(NumberPicturesInArray):
    if PictureArray[x].GetColour() == usercolour:
        if PictureArray[x].GetWidth() <= userWidth:
            if PictureArray[x].GetHeight() <= userHeight:
                print(PictureArray[x].GetDescription(), PictureArray[x].GetWidth(), PictureArray[x].GetHeight(), PictureArray[x].GetColour())

# binary tree picture
def AddNode(ArrayNode, RootPointer , FreeNode):
    NodeData = int(input("Enter the Data: "))
    if FreeNode <= 19:
        ArrayNode[FreeNode][0] = -1
        ArrayNode[FreeNode][1] = NodeData
        ArrayNode[FreeNode][2] = -1
        if RootPointer == -1:
            RootPointer = 0
        else:
            Placed = False
            CurrentNode = RootPointer
            while not Placed:
                if NodeData < ArrayNode[CurrentNode][1]:
                    if ArrayNode[CurrentNode][0] ==-1 :
                        ArrayNode[CurrentNode][0] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNode[CurrentNode][0]
                else:
                    if ArrayNode[CurrentNode][2] == -1:
                        ArrayNode[CurrentNode][2] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNode[CurrentNode][2]
        FreeNode += 1
    else:
        print("Tree is full")
    return ArrayNode, RootPointer, FreeNode


    
def printAll(ArrayNode):
    for x in range(0,20):
        print(ArrayNode[x][0]," ", ArrayNode[x][1], " ", ArrayNode[x][2])
ArrayNode = [[0 for x in range (3)] for y in range (20)] #integer
RootPointer = -1 #integer
FreeNode = 0 #integer
for x in range (10):
    ArrayNode,RootPointer,FreeNode = AddNode(ArrayNode, RootPointer, FreeNode)
printAll(ArrayNode)

def inOrder(ArrayNode, RootNode):
    if ArrayNode[RootNode][0] != -1:
        inOrder(ArrayNode, ArrayNode[RootNode][0])
    print(str(ArrayNode[RootNode][1]))
    if ArrayNode[RootNode][2]!= -1:
        inOrder(ArrayNode,ArrayNode[RootNode][2])

inOrder(ArrayNode,RootPointer)

# Card paper
# stack
def OutputValues():
    print("StackPointer: ", StackPointer)
    for x in range(0,10):
        print(StackData[x])
def Push(userInput):
    global StackData, StackPointer
    if StackPointer == maxStack:
        return False
    else:
        StackData[StackPointer] = userInput
        StackPointer += 1
        return True
def Pop():
    global StackData, StackPointer
    if StackPointer == 0:
        return -1
    elif StackPointer <= maxStack:
        StackPointer -=1
        valueTop = StackData[StackPointer]
        StackData[StackPointer] = 0
        return valueTop
global StackData #integer
global StackPointer
StackData = [0,0,0,0,0,0,0,0,0,0] #integer
StackPointer = 0
maxStack = 10
for x in range(0,11):
    userInput = int(input("Enter a number to push: "))
    if Push(userInput) == True:
        print("Added")
    else:
        print("Stack full")
OutputValues()
print(StackData)
Pop()
Pop()
Pop()
Pop()
print(StackData)
print(Pop)

# bubble sort and binary search
import random
arrayLength = 10
arrayData = [[random.randint(0,100)for i in range(arrayLength)]for j in range(arrayLength)]
def printMethod():
    for x in range(0, 10):
        for y in range(0, 10):
            print(arrayData[x][y], " ", end='')
        print("") 
printMethod()
for x in range(0,arrayLength):
    for y in range(0,arrayLength):
        for z in range(0, arrayLength -y- 1):
            if arrayData[x][z]>arrayData[x][z+1]:
                arrayData[x][z], arrayData[x][z+1] = arrayData[x][z+1], arrayData[x][z]
print("///")                
printMethod()

def BinarySearch(SearchArray, Lower, Upper, SearchValue):
    if Upper >= Lower:
        Mid = (Lower+(Upper+1))//2
        if SearchArray[0][Mid] == SearchValue:
            return Mid
        else:
            if SearchArray[0][Mid] > SearchValue:
                return BinarySearch(SearchArray, Lower, Mid-1, SearchValue)
            else:
                return BinarySearch(SearchArray, Mid+1, Upper, SearchValue)
    return -1
SearchValue = int(input("Enter a value:"))
print(BinarySearch(arrayData,0,arrayLength-1,SearchValue))

# Card
class card:
    #Number as Integer
    #Colour as String
    def __init__(self, Number, Colour):
        self.__Number = Number
        self.__Colour = Colour
    
    def GetNumber(self):
        return self.__Number
    
    def GetColour(self):
        return self.__Colour

cardArray = [0 for i in range (30)]

def chooseCard():
    global NumberChosen
    flagContinue = True
    while flagContinue:
        userCard = int(input("Enter a card number: "))
        if userCard < 1 or userCard > 30:
            print("Number must be between 1 and 30")
        elif NumberChosen[userCard-1]:
            print("Card already chosen")
        else:
            print("Card chosen: ", userCard)
            flagContinue = False
            NumberChosen[userCard-1] = True
    return userCard - 1

filename = "CardValues.txt"
try:
    with open(filename,"r") as File:
        for x in range(30):
            Number = int(File.readline())
            Colour = File.readline().strip()
            cardArray[x] = card(Number, Colour)
except FileNotFoundError:
    print("file not found")

NumberChosen = [False for i in range(30)]
Player1 = []

for x in range(0,4):
    player1num = chooseCard()
    Player1.append(cardArray[player1num])

for x in range(0,4):
    print(Player1[x].GetNumber())
    print(Player1[x].GetColour())

# Employee paper Employees
# Circular queue
class SaleData:
    def __init__(self,SaleID,quantity):
        self.saleID = SaleID #STRING
        self.saleQuantity = quantity #INTEGER

circularQueue = [] # Array saledata 5 items
Head = 0
Tail = 0
NumberOfItems = 0
for x in range (0,5):
    circularQueue.append(SaleData("",-1))

def Enqueue(value):
    global circularQueue,Head,Tail,NumberOfItems
    if NumberOfItems == 5:
        return -1
    else:
        circularQueue[Tail] = value
        if Tail == 4:
            Tail = 0
        else:
            Tail +=1
        NumberOfItems +=1
        return 1
        
def Dequeue():
    global circularQueue,Head,Tail,NumberOfItems
    recordRemoved = SaleData("",-1)
    if NumberOfItems == 0:
        return recordRemoved
    else:
        recordRemoved = circularQueue[Head]
        NumberOfItems -= 1
        if Head == 4:
            Head = 0
        else:
            Head += 1
        return recordRemoved
    
def EnterRecord():
    ID = input("Enter ID: ")
    Quantity = int(input("Enter quantity: "))
    item = SaleData(ID,Quantity)
    if Enqueue(item) == -1:
        print("Full")
    else:
        print("Stored")

EnterRecord()
EnterRecord()
EnterRecord()
EnterRecord()
EnterRecord()
EnterRecord()
returnValue = Dequeue()
if returnValue.saleID == "":
    print("No items")
else:
    print("Removed record: ",returnValue.saleID,returnValue.saleQuantity)
EnterRecord()
for x in range(0,5):
    print("ID: ",circularQueue[x].saleID,"Quantity",circularQueue[x].saleQuantity)

# Employees 
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