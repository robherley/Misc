'''
Created By Rob Herley on 9.20.16
A really shitty program that calculates various info about an iP Address
'''
def binary(ip_int):
    '''Accepts a decimal string and returns the binary byte'''
    newBin = bin(ip_int)[2:]
    if len(newBin) < 8:
        newBin = "0"*(8 - len(newBin)) + newBin
    return newBin

def ip_to_binary(str_ip):
    '''Accepts a iP string and returns binary address'''
    str_ip += "."
    newStr = ""
    partNumStr = ""
    for letter in str_ip:
        if letter == ".":
            newStr += str(binary(int(partNumStr))) + letter
            partNumStr = ""
        elif letter != ".":
            partNumStr += letter
    return newStr[:-1]

def network_class(bin_ip):
    '''Accepts a binary ip and returns the classful address'''
    print("\n Note: Classful Addresses have not been used since 1981 \n")
    fourbit = bin_ip[:4]
    if fourbit[:1] == "0":
        print("Class A: \
                    \n Number of Networks: 128 \
                    \n Addresses per Network: 16,777,216 \
                    \n Total Addresses in Class A: 2,147,483,648 \
                    \n Start Address: 0.0.0.0 \
                    \n End Address: 127.255.255.255")
    elif fourbit[:2] == "10":
        print("Class B: \
                    \n Number of Networks: 16,384 \
                    \n Addresses per Network: 65,536 \
                    \n Total Addresses in Class B: 1,073,741,824 \
                    \n Start Address: 128.0.0.0 \
                    \n End Address: 191.255.255.255")
    elif fourbit[:3] == "110":
        print("Class C: \
                    \n Number of Networks: 2,097,152 \
                    \n Addresses per Network: 256 \
                    \n Total Addresses in Class C: 536,870,912 \
                    \n Start Address: 192.0.0.0 \
                    \n End Address: 223.255.255.255")
    elif fourbit[:4] == "1110":
        print("Class D: \
                    \n Number of Networks: not defined \
                    \n Addresses per Network: not defined \
                    \n Total Addresses in Class D: 2^28 \
                    \n Start Address: 224.0.0.0 \
                    \n End Address: 239.255.255.255 \
                    \n \n Note: Class D is multicast")
    elif fourbit[:4] == "1111":
        print("Class E: \
                    \n Number of Networks: not defined \
                    \n Addresses per Network: not defined \
                    \n Total Addresses in Class E: 2^28 \
                    \n Start Address: 240.0.0.0 \
                    \n End Address: 255.255.255.255 \
                    \n \n Note: Class E is reserved")

def CIDR_bin(intCIDR):
    newCIDR = "1" * intCIDR
    if len(newCIDR) < 32:
        newCIDR = newCIDR + "0" * (32-len(newCIDR))
    return newCIDR[:8] + '.' + newCIDR[8:16] + '.' + newCIDR[16:24] + '.' + \
            newCIDR[24:32]

def CIDR_info(intCIDR):
    print("Subnet mask in Binary:" + str(CIDR_bin(intCIDR)))

if __name__ == '__main__':
    ip_address = input("Enter an IP Address:")
    print("Binary: " + str(ip_to_binary(ip_address)))
    network_class(str(ip_to_binary(ip_address)))
