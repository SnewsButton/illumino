from ip_address_manager import IpAddressManager

zero = '0.0.0.0'
lower = '0.0.10.250'
upper = '0.0.11.0'
ip_range = lower + '-' + upper
upper_overlap = '0.0.10.254'
ip_range_overlap = lower + '-' + upper_overlap

def test_ip_address_manager():
    print('Test ip address manager:')
    test_add_single()
    test_add_range()
    test_get_rules()

def test_add_single():
    print('Test add_single():')
    ip_manager = IpAddressManager()
    ip_manager.add(zero, 0)
    print(zero in ip_manager.rule_store)
    print(ip_manager.rule_store[zero] == {0})

def test_add_range():
    print('Test add_range()')
    ip_manager = IpAddressManager()
    ip_manager.add(ip_range, 0)
    print(len(ip_manager.rule_store) == 7)
    print(lower in ip_manager.rule_store)
    print(upper in ip_manager.rule_store)
    print(ip_manager.rule_store)

    ip_manager.add(ip_range_overlap, 1)
    print(len(ip_manager.rule_store) == 7)

    print(len(ip_manager.rule_store[lower]) == 2)
    print(len(ip_manager.rule_store[upper_overlap]) == 2)
    print(len(ip_manager.rule_store[upper]) == 1)
    print(ip_manager.rule_store)

def test_get_rules():
    print('Test get_rules():')
    ip_manager = IpAddressManager()
    ip_manager.add(ip_range, 0)
    ip_manager.add(ip_range_overlap, 1)
    print(ip_manager.get_rules(zero) == set())
    print(ip_manager.get_rules(lower) == {0, 1})
    print(ip_manager.get_rules(upper_overlap) == {0, 1})
    print(ip_manager.get_rules(upper) == {0})

test_ip_address_manager()
