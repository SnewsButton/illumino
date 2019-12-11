from ip_address import IpAddress

zero = '0.0.0.0'
carry_over = '9.255.255.255'
one_to_max = '255.255.255.254'

zero_ip = IpAddress(zero)
carry_over_ip = IpAddress(carry_over)
one_to_max_ip = IpAddress(one_to_max)

def test_ip_address():
    print('TEST IP ADDRESS:')
    test_str()
    test_is_less_than_or_equal_to()
    test_increment()

def test_str():
    print('Test initialization:')
    print(zero == str(zero_ip))
    print(carry_over == str(carry_over_ip))
    print(one_to_max == str(one_to_max_ip))

def test_is_less_than_or_equal_to():
    print('Test is_less_than_or_equal_to():')
    print(zero_ip.is_less_than_or_equal_to(zero_ip) == True)
    print(zero_ip.is_less_than_or_equal_to(carry_over_ip) == True)
    print(zero_ip.is_less_than_or_equal_to(one_to_max_ip) == True)

    print(carry_over_ip.is_less_than_or_equal_to(zero_ip) == False)
    print(carry_over_ip.is_less_than_or_equal_to(carry_over_ip) == True)
    print(carry_over_ip.is_less_than_or_equal_to(one_to_max_ip) == True)

    print(one_to_max_ip.is_less_than_or_equal_to(zero_ip) == False)
    print(one_to_max_ip.is_less_than_or_equal_to(carry_over_ip) == False)
    print(one_to_max_ip.is_less_than_or_equal_to(one_to_max_ip) == True)

def test_increment():
    print('Test increment():')
    zero_ip.increment()
    carry_over_ip.increment()
    one_to_max_ip.increment()

    print(str(zero_ip) == '0.0.0.1')
    print(str(carry_over_ip) == '10.0.0.0')
    print(str(one_to_max_ip) == '255.255.255.255')

test_ip_address()
