
'''
these codes are the example of the
composition

Sedan class inherits from the car class 
and  is a part-of the SedanEngine
sedan and sedanengine has a partof relationship(composition)
sedan is the owner class
sedan engine is the owned object

owned object is a partof OwnerClass.

owner class owns the lifetime of the owned object in the composition .


'''
class Car:
 def __init__(self,model,color):
  self.model=model
  self.color=color
 def printDetails(self):
  print('mode is ',self.model)
  print('color is ',self.color)
  
class Sedan(Car):
 def __init__(self,model,color):
  super().__init__(self,model,color)
  self.engine=SedanEngine()
 def setStart(self):
  self.engine.start()
 def setStop(self):
  self.engine.stop()
  
class SedanEngine:
 def start(self):
  print('car has started')
 def stop(self):
  print('car has stopped')
  
'''
owner class has a owned object 

'''

class School:
    def __init__(self,schoolName=None):
        self.teams=[]
        self.schoolName=schoolName
    
    def getTotalPlayersInSchool(self):
        length=0
        for n in self.teams:
            length+=(n.getPlayers())
        return length
    
    def addTeam(self,team):
        self.teams.append(team)
        
    
class  Team:
    def __init__(self,name=None):
        self.players=[]
        self.name=name
    def addPlayers(self,player):
        self.players.append(player)
    def getPlayers(self):
        return len(self.players)
    

class Player:
    def __init__(self,name,teamName,ID):
        self.ID=ID
        self.teamName=teamName
        self.name=name
        

if __name__ == '__main__':
    p1 = Player("Harris", 1, "Red")
    p2 = Player("Carol", 2, "Red")
    p3 = Player("Johnny", 1, "Blue")
    p4 = Player("Sarah", 2, "Blue")
    red_team=Team("Red Team")
    red_team.addPlayers(p1)
    red_team.addPlayers(p2)
    blue_team=Team("Blue Team")
    blue_team.addPlayers(p3)
    blue_team.addPlayers(p4)
    mySchool=School("My School")
    mySchool.addTeam(red_team)
    mySchool.addTeam(blue_team)
    print("Total players in my school:", mySchool.getTotalPlayersInSchool())


    
    
    