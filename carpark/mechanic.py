
class Mechanic: 
    def __init__(self, carBrand, carMake, carColour, carBodyType):
        self.carBrand = carBrand
        self.carMake = carMake
        self.carColour = carColour
        self.carBodyType = carBodyType

        
class CarModel:
    def __init__(self, carNationality, carBrand, carModel ):
        self.carNationality = carNationality
        self.carBrand = carBrand
        self.carModel = carModel
    def getID(self):
        return F"{self.carBrand}_{self.carModel}".lower()
    

class CarRegistry:
    def __init__(self):
        self.carRegistery = []
    def registerCar(self, car: Car):
        self.carRegistery.append(car)   
    def showRegister(self):
        for car in self.carRegistery:
            print(f"Car Registry: {car.carBrand} {car.carModel} - {car.carColour} {car.carBodyType} {car.noPlate} {car.buildDate}")



class CarModelDataBase:
    def __init__(self):
        models = [
            CarModel("Gernany", "Audi", "TT"),
        ]
        #Using a dictionary comprehension
        self.models = {model.getID(): model for model in models   } 

class ClientDataBase:
    def __init__(self):
        self.clients = []
 

class Service:
    def __init__(self, car: Car):
        self.car = car
        self.baseServicePrice = self.setBaseServicePrice()
        
class Logbook:
    def __init__(self):
        self.entries=[]
    def addLog(self,newLog):
        self.entries.append(newLog)
    
        
class LogbookEntry():
    def __init__(self, notes, service_date):
        self.notes = notes
        self.service_date = service_date



    
    


car1 = Car("Grey", "SUV", "DGA99Y", "2008")


employee1 = Employee("Alice", "NSW123456")
client1 = Client("Elizabeth", "NSW1234")

 

print(employee1.EmployeeID) 
print(client1.ClientID)  
