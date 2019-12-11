from property_manager import PropertyManager

class PortManager(PropertyManager):

    def __init__(self):
        self.rule_store = {}

    def add(self, value, rule_number):
        if '-' in value:
            self.add_range(value, rule_number)
        else:
            self.add_single(int(value), rule_number)

    # We store every port number enumerated by the range
    def add_range(self, value, rule_number):
        split_port = value.split('-')
        lower, upper = int(split_port[0]), int(split_port[1])

        while lower <= upper:
            self.add_single(lower, rule_number)
            lower += 1

    def add_single(self, value, rule_number):
        if value not in self.rule_store:
            self.rule_store[value] = set()

        self.rule_store[value].add(rule_number)

    def get_rules(self, value):
        value_int = int(value)
        if value_int in self.rule_store:
            return self.rule_store[value_int]
        else:
            return set()
    

