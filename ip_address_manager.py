from property_manager import PropertyManager
from ip_address import IpAddress

class IpAddressManager(PropertyManager):

    def __init__(self):
        self.rule_store = {}

    def add(self, value, rule_number):
        if '-' in value:
            self.add_range(value, rule_number)
        else:
            self.add_single(value, rule_number)
    
    # We store every ip address enumerated by the range
    def add_range(self, value, rule_number):
        split_ip = value.split('-')
        curr_ip, upper_ip = IpAddress(split_ip[0]), IpAddress(split_ip[1])

        while curr_ip.is_less_than_or_equal_to(upper_ip):
            curr_ip_str = str(curr_ip)
            if curr_ip_str not in self.rule_store:
                self.rule_store[curr_ip_str] = set()

            self.rule_store[curr_ip_str].add(rule_number)
            curr_ip.increment()

    def add_single(self, value, rule_number):
        if value not in self.rule_store:
            self.rule_store[value] = set()

        self.rule_store[value].add(rule_number)

    def get_rules(self, value):
        if value in self.rule_store:
            return self.rule_store[value]
        else:
            return set()
