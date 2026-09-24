import socket

def checksum(data):
    return (~sum(map(ord, data))) & 0xFFFF

s = socket.socket()
s.connect(("localhost", 5000))

data = input("Enter data: ")
c = checksum(data)

s.send(data.encode())
s.send(str(c).encode())

print("Checksum sent:", c)
print("Server:", s.recv(1024).decode())

s.close()