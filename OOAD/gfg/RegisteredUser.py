
class RegisteredUser(User):
    
    def __init__(self,userId,name,password):
        super().__init__(userId,name,password)
        self.bookingHistory = list()
        
    def login(self,userId,Username):
        '''
        method to authenticate the user based on some credentials either JWT or OAuth.
        '''
        pass
    
    def cancelTicket(self):
        '''
        method to cancel the booked ticket
        '''
        pass
    
    def getUserId(self):
        super().getUserId()
    
    def getUserName(self):
        super().getUserName()
    
    
    #registeredUser has bookinghistory how should we show this ?