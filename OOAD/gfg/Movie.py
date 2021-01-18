from enum import Enum


#how to show the aggregation with the Movie-class and the enum?
class Genre(Enum):
    ACTION=1
    ROMANCE=2
    COMEDY=3
    HORROR=4
    
class Language(Enum):
    ENGLISH=1
    HINDI=2
    
    
class Movie:
    def __init__(self,name,ratings,language,genre):
        self.__name=name
        self.__ratings=ratings
        self.__language=language
        self.__genre=genre
    
    def getName(self):
        return self.__name
    
    def getRatings(self):
        return self.__ratings
    
    def getLaguage(self):
        return self.__language
        
        

    
    