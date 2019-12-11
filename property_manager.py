
from abc import ABC, abstractmethod

class PropertyManager(ABC):
    
    @abstractmethod
    def add(self, value, rule_number):
        pass

    @abstractmethod
    def get_rules(self, value):
        pass
