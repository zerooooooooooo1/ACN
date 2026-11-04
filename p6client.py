
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

data = input("Enter data: ")
checksum = (~sum(data.encode())) & 0xFFFF

s.sendto(f"{data}|{checksum}".encode(), ('localhost', 5000))
print("Checksum:", checksum)
print("Data sent successfully")
