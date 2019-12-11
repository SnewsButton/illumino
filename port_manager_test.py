from port_manager import PortManager

zero = '0'
hundred = '99'
first_hundred = zero + '-' + hundred

def test_port_manager():
    print('Test port manager:')
    test_add_single()
    test_add_range()
    test_get_rules()

def test_add_single():
    print('Test add_single()')
    port_manager = PortManager()
    port_manager.add(zero, 0)
    port_manager.add(hundred, 1)
    port_manager.add(zero, 2)

    print(port_manager.rule_store[0] == {0, 2})
    print(port_manager.rule_store[99] == {1})
    print(len(port_manager.rule_store) == 2)

def test_add_range():
    print('Test add_range()')
    port_manager = PortManager()
    port_manager.add(first_hundred, 2)

    print(len(port_manager.rule_store) == 100)
    print(port_manager.rule_store[0] == {2})
    print(port_manager.rule_store[99] == {2})

def test_get_rules():
    print('Test get_rules()')
    port_manager = PortManager()
    port_manager.add(first_hundred, 3)
    port_manager.add(zero, 0)

    print(port_manager.get_rules('100') == set())
    print(port_manager.get_rules('0') == {0, 3})

test_port_manager()