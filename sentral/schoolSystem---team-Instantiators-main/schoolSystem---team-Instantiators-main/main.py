#This is the main program code

#Import classes from external files - the first one is done - you add the rest
from headTeacher import *
from highSchoolStudent import *
from mark import *
from person import *
from primaryStudent import *
from staff import *
from student import *
from subject import *
from task import *
from teacher import *

#Define any subprograms you might need here


#The mainline program code 
#Test the classes by adding one object of each and interacting with their methods to ensure they behave correctly
person=Person("Person!")
print(person.info()

staff=Staff("Staff", 13090)
print(staff.info())
staff.giveRaise(1000)
print(staff.info())

