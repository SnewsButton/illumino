from property_manager import PropertyManager
'''
This manager is used for direction and protocol 
rule management
'''
class SimpleManager(PropertyManager):

    def __init__(self):
        self.rule_store = {}

    def add(self, value, rule_number):
        if value not in self.rule_store:
            self.rule_store[value] = set()
        self.rule_store[value].add(rule_number)

    def get_rules(self, value):
        if value in self.rule_store:
            return self.rule_store[value]
        else:
            return set()

