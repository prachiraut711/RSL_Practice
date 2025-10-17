# write program for ip address

# what you mean by “program for IP address” — there are a few common types:
# 1.Validate an IP address (check if it’s valid IPv4 or not)
# 2.Find your system’s IP address (using Python)
# 3.Convert string to IP format / split into parts

# If you can, ask the interviewer:
# “Do you want me to validate an IP address, display the system’s IP, or process an IP string?”
# That shows clarity and professionalism.
# If they say “Find the system’s IP” → use the socket method.
# If they say “Check IP validity” → use the validation logic.
# But if they don’t clarify (and just say "write program for IP address"),
# then the safe and most expected answer is:
# Program to find the system’s IP address (your machine’s IP).
# That’s the one asked most often in short tech rounds.


# 2.Get Your Computer’s IP Address
import socket

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

print("Hostname: ", hostname)
print("ip_address: ", ip_address)

print("_______")
# 1.Validate an IP Address (IPv4)
# Checks if a given string is a valid IPv4 address (like 192.168.1.1).
def is_valid_ip(ip):
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    for i in parts:
        if not i.isdigit():
            return False
        num = int(i)
        if num < 0 or num > 255:
            return False
    return True
# Test
print(is_valid_ip("192.168.0.1"))   # True
print(is_valid_ip("256.100.10.1"))  # False
print(is_valid_ip("192.168.1"))     # False


print("_______")
# 3. Split an IP Address into Octets
ip = "192.168.1.10"
parts = ip.split(".")
for i, part in enumerate(parts, 1):   #jar only parts function madhe dil ast tar 0,1,2,3 she i ale aste but by giving parts,1 parameter now i = 1,2,3,4
    print(f"octate {i} : {part}")
