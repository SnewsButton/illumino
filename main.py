from firewall import Firewall

fw = Firewall('./test_files/sample_small.csv')
print(fw.accept_packet("inbound", "tcp", 80, "192.168.1.2"))