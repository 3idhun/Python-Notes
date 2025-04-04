'''

Q5. Write a class Train which has methods to book a
    ticket, get status and get fare information of train
    running under Indian railways.


'''

from random import randint

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to): #using "pass" after this line and editing after is best.
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time")

    def getFare(self, fro, to):
        print(f"Train fare in train no: {self.trainNo} from {fro} to {to} is {randint(222, 5555)}") #if randint is not imported first use random.randint


t = Train(12399)
t.book("Delhi", "Bengaluru")
t.getStatus()
t.getFare("Delhi", "Bangalore")