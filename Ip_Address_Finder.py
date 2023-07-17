import socket

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

print("Your Computer Name is :-"+ hostname)
print("Your Computer IP Add is :-"+ IPAddr)

from ip2geotools.databases.noncommercial import DbIpCity

def printDetails(ip):
    res =DbIpCity.get(ip,api_key="free")
    print(f"IP Address : {res.ip_address}")
    print(f"Location: {res.city}, {res.region},{res.country}")
    print(f"Coordinates: (Lat:{res.latitude}, lng:{res.longitude})")

ip_add = input("Enter Ip Address:-")
printDetails(ip_add)