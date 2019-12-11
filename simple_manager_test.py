from simple_manager import SimpleManager

tcp = 'tcp'
udp = 'udp'

def test_simple_manager_test():
    print('Test simple manager')
    test_add()
    test_get_rules()

def test_add():
    print('Test add()')
    manager = SimpleManager()
    manager.add(tcp, 10)
    manager.add(tcp, 12)
    manager.add(udp, 15)

    print(manager.rule_store[tcp] == {10, 12})
    print(manager.rule_store[udp] == {15})

def test_get_rules():
    print('Test get_rules()')
    manager = SimpleManager()
    manager.add(tcp, 10)
    manager.add(tcp, 12)
    manager.add(udp, 15)

    print(manager.get_rules(tcp) == {10, 12})
    print(manager.get_rules(udp) == {15})
    print(manager.get_rules('not a key') == set())

test_simple_manager_test()