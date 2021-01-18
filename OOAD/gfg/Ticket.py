class Ticket:
    '''
    ticket class which provides the information for ticket related information
    
    :id 
    '''
    
    def __init__(self,id,bookingTime,theater,numberofSeats):
        self.__id=id
        self.__bookingTime=bookingTime
        self.__theater=theater
        self.__numberofSeats=numberofSeats
    
    
    def getTicketInfo(self):
        '''
        return:= Ticket
        '''
        pass
    
    def cancelTicket(self):
        '''
        return: int
        '''
        pass