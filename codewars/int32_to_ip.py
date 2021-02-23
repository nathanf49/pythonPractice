"""
Take the following IPv4 address: 128.32.10.1

This address has 4 octets where each octet is a single byte (or 8 bits).

    1st octet 128 has the binary representation: 10000000
    2nd octet 32 has the binary representation: 00100000
    3rd octet 10 has the binary representation: 00001010
    4th octet 1 has the binary representation: 00000001

So 128.32.10.1 == 10000000.00100000.00001010.00000001

Because the above IP address has 32 bits, we can represent it as the unsigned 32 bit number: 2149583361

Complete the function that takes an unsigned 32 bit number and returns a string representation of its IPv4 address.
"""

def int32_to_ip(int32):
    bit = 31
    ip = ''
    while bit >= 0:
        if int32 >= 2 ** bit: # use the bits when possible, signified by 1 and subtracting the value of the bit
            ip += '1'
            int32 -= 2 ** bit
        else: # use a 0 and wait for a smaller bit
            ip += '0'
        bit -= 1 # move onto the next bit regardless of whether or not we could use current
    return str(int(ip[0:8],2)) + '.' + str(int(ip[8:16],2)) + '.' + str(int(ip[16:24],2)) + '.' + str(int(ip[24:],2))


"""
CodeWars Tests:
int32_to_ip(2154959208), "128.114.17.104" 
int32_to_ip(0), "0.0.0.0"
int32_to_ip(2149583361), "128.32.10.1"
"""