from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def get_name(self):
        pass
    @abstractmethod
    def set_name(self, new):
         pass

    @abstractmethod
    def get_password(self):
        pass
    @abstractmethod
    def set_password(self, new):
        pass
    
    @abstractmethod
    def get_key(self):
        pass
