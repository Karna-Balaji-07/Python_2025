# Validate an IP address

def IPaddress1(s):
    n = len(s)
    if n > 3:
        return False
    for i in range(n):
        if not s[i].isdigit():
            return False
    x = int(s)
    return 0 <= x <= 255

def isValid(ip):
    if ip is None:
        return False
    parts = ip.split(".")
    count = 0
    for i in range(len(ip)):
        if ip[i] == '.':
            count += 1
    if count != 3:
        return False
    for part in parts:
        if not IPaddress1(part):
            return False
    return True

#-------------------------------------------------------------------------------------------------#
def in_range(n):
    if n >= 0 and n <= 225:
        return True
    return False
def has_leading_zeros(n):
    if len(n) > 1:
        if n[0] == "0":
            return True
    return False

def isValid1(ip):
    s = ip.split(".")
    if len(s) != 4:
        return False
    for i in s:
        if has_leading_zeros(i):
            return False
        if len(i) == 0:
            return False
        try:
            n = int(i)
            if not in_range(n):
                return False
        except:
            return False
    return True

         


ip2 = "125.16.100.1"
ip3 = "125.512.100.1"
ip4 = "0.0.0.255"
print(isValid1(ip2))
print(isValid1(ip3))
print(isValid1(ip4))