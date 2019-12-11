from firewall import Firewall

sample_small = './test_files/sample_small.csv'
sample_large = './test_files/sample_large.csv'

def test_firewall():
    print('Test firewall')
    test_sample_small()
    test_sample_large()

def test_sample_small():
    print('Test firewall with', sample_small)

    fw = Firewall(sample_small)
    print(fw.accept_packet("inbound", "tcp", 80, "192.168.1.2") == True)
    print(fw.accept_packet("inbound", "udp", 53, "192.168.2.1") == True)
    print(fw.accept_packet("outbound", "tcp", 10234, "192.168.10.11") == True)

    print(fw.accept_packet("inbound", "tcp", 81, "192.168.1.2") == False)
    print(fw.accept_packet("inbound", "udp", 24, "52.12.48.92") == False)
    print(fw.accept_packet("inbound", "tcp", 80, "192.168.1.3") == False)

def test_sample_large():
    print('Test firewall with', sample_large)
    fw = Firewall(sample_large)
    print(fw.accept_packet("inbound", "tcp", 80, "192.168.1.2") == True)
    print(fw.accept_packet("inbound", "udp", 53, "192.168.2.1") == True)
    print(fw.accept_packet("outbound", "tcp", 10234, "192.168.10.11") == True)

    print(fw.accept_packet("inbound", "tcp", 81, "192.168.1.2") == False)
    print(fw.accept_packet("inbound", "udp", 24, "52.12.48.92") == False)
    print(fw.accept_packet("inbound", "tcp", 80, "192.168.1.3") == False)

    print(fw.accept_packet("outbound", "tcp", 0, "0.0.0.0") == True)
    print(fw.accept_packet("outbound", "tcp", 0, "0.0.255.255") == True)

    print(fw.accept_packet("outbound", "tcp", 10, "0.0.0.0") == False)
    print(fw.accept_packet("outbound", "tcp", 10, "0.0.255.255") == False)
    print(fw.accept_packet("outbound", "tcp", 0, "0.1.0.0") == False)

test_firewall()
