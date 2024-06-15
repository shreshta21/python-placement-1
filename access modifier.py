class Super:
    
    #public data member
    var1=None
    
    #protected data member
    _var2=None
    
    #private data member
    __var3=None
    
    #constructor
    def __init__(self,var1,var2,var3):
        self.var1=var1
        self._var2=var2
        self.__var3=var3
        
    #public member function
    
    def displayPublicMembers(self):
        
        #accessing public data members
        print("public data member:",self.var1)
    
        #protected member function    
    def _displayProtectedMembers(self):
        
       #accessing protected data members
        print("protected data member:",self._var2)
       
       #private member function    
    def _displayPrivateMembers(self):
        
     #accessing private data members
        print("private data member:",self.__var3)
        
     #public member function   
    def accessPrivateMembers(self):
        #accessing private  members function
        self._displayPrivateMembers()
        
class Sub(Super):
    
    #constructor
    def __init__(self,var1,var2,var3):
        Super.__init__(self,var1,var2,var3)
        
    #public member function 
    def accessProtectedMembers(self):
        #accessing protected member function of super class
        self._displayProtectedMembers()
        
obj=Sub("Hello","all","people !")

#calling public member functions of the class
obj.displayPublicMembers()
obj.accessProtectedMembers()
obj.accessPrivateMembers()

#object can access protected member
print("object is accessing protected member:",obj._var2)
   
#object can not access private member,so it will generate attribute

##print(__var3)     
        