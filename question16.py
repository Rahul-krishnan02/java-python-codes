
class student:


    def __init__(self,name1,regno1,branch1 ):
        self.name=name1
        self.regno=regno1
        self.branch=branch1
    def printdetails(self):
        print( self.name, self.regno,self.branch)

class MIT:
    deets = student("rahul","200907336","ECE")
    deets.printdetails()
