#Create a Subject class in this file
#Accept and assign agreed parameters in the constructor and define agreed public methods in the class
#Program the class so that users of the class only need to interact with its methodsfrom person import *

class Student(Person):
    def __init__(self, name, schoolYear):
        super().__init__(name)
        self.schoolYear = schoolYear
      
    
    def getSchoolYear(self):
        return self.schoolYear 
    def setSchoolYear(self, schoolYear):
        self.schoolYear = schoolYear
    def nextSchoolYear(self):
        self.schoolYear = self.schoolYear+1
        
        