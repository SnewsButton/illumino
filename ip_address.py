
class IpAddress():
    MAX_DIGIT = 256

    def __init__(self, ip_string):
        self.ip_string = ip_string
        self.ip_arr = []
        self.convert_ip_string()

    def convert_ip_string(self):
        ip_string_split = self.ip_string.split('.')
        self.ip_arr = [int(num) for num in ip_string_split]

    # determines if self <= ip_address
    def is_less_than_or_equal_to(self, ip_address):
        for i in range(len(self.ip_arr)):
            num_1 = self.ip_arr[i]
            num_2 = ip_address.ip_arr[i]

            if num_1 < num_2:
                return True
            elif num_1 > num_2:
                return False
        
        return True # equal
    
    # increment an IpAddress by just one.
    # Assume 255.255.255.255 will not be incremented
    def increment(self):
        carry_over = 1
        for i in reversed(range(len(self.ip_arr))):
            self.ip_arr[i] += carry_over
            carry_over = int(self.ip_arr[i] / IpAddress.MAX_DIGIT)
            self.ip_arr[i] = self.ip_arr[i] % IpAddress.MAX_DIGIT

    def __str__(self):
        return '.'.join([str(num) for num in self.ip_arr])
