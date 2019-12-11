from simple_manager import SimpleManager
from port_manager import PortManager
from ip_address_manager import IpAddressManager

DIRECTION = 'direction'
PROTOCOL = 'protocol'
PORT = 'port'
IP_ADDRESS = 'ip address'

class Firewall():

    property_order = [DIRECTION, PROTOCOL, PORT, IP_ADDRESS]

    def __init__ (self, rule_file):
        self.rule_file = rule_file
        self.rule_managers = {
            DIRECTION: SimpleManager(),
            PROTOCOL: SimpleManager(),
            PORT: PortManager(),
            IP_ADDRESS: IpAddressManager()
        }
        self.preprocessing()

    def preprocessing(self):
        print('Start of preprocessing')
        with open(self.rule_file) as fp:
            rule = fp.readline().rstrip()
            rule_number = 1
            while rule:
                self.add_rule(rule, rule_number)
                rule = fp.readline().rstrip()
                rule_number += 1
        
        print('End of preprocessing')
    
    def add_rule(self, rule, rule_number):
        rule_properties = rule.split(',')

        # gives each property of the rule to its respective manager
        for i in range(len(rule_properties)):
            prop = Firewall.property_order[i]
            prop_value = rule_properties[i]
            self.rule_managers[prop].add(prop_value, rule_number)
    
    def accept_packet(self, direction, protocol, port, ip_address):
        # for each property, we take the intersection of all the rules a property
        # satisfies, if the resultant set is empty, then the packet is not allowed
        prop_arr = [direction, protocol, str(port), ip_address]
        valid_rules = self.rule_managers[DIRECTION].get_rules(direction)
        
        for i in range(1, len(prop_arr)):
            if len(valid_rules) == 0:
                return False

            prop = Firewall.property_order[i]
            prop_value = prop_arr[i]

            prop_rule = self.rule_managers[prop].get_rules(prop_value)
            valid_rules = valid_rules.intersection(prop_rule)

        return len(valid_rules) != 0
