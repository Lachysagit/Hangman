
from person import *

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
        