from abc import ABC , abstractmethod

class Nguoi(ABC):
    def __init__(self , name="" , address=""):
        self.__name = name 
        self.__address = address

    @abstractmethod
    def nhan_xet():
        pass

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    def get_address(self):
        return self.__address

    def set_address(self, value):
        self.__address = value
    
    def __str__(self):
        return f"name: {self.get_name()} address: {self.get_address()}"
    
    
        