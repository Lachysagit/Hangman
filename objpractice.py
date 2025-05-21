
class Footballer:
    nationalityScores={"brasil":12, "argentina":10, "Portugese":8, "pom":2}
    
    
    
    
    
    
    def __init__(self, streetsKnowledge, nationality, editability, trophies, skillMoves, height, shirtNo):
        self.__height = height
        self.aura=10
        self.streetsKnowledge = streetsKnowledge
        self.nationality = nationality
        self.editability = editability
        self.trophies = trophies
        self.skillMoves = skillMoves
        self.shirtNo = shirtNo
        
        if self.__height < 5.8:
            aura_loss= 5.8 - height 
            
            self.aura = self.aura - aura_loss
        
        
        
        if self.nationality not in self.nationalityScores:
            print("true")
    
      
       
        
    def getHeight(self):
        return(self.__height)
    
    print(self)