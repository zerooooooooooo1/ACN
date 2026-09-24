import socket

def checksum(data):
    return (~sum(map(ord, data))) & 0xFFFF

s = socket.socket()
s.bind(("localhost", 5000))
s.listen(1)

print("Server waiting...")
c, addr = s.accept()

data = c.recv(1024).decode()
received = int(c.recv(1024).decode())

calculated = checksum(data)

print("Received data:", data)
print("Received checksum:", received)
print("Calculated checksum:", calculated)

if received == calculated:
    c.send(b"Data is correct - Checksum verified")
else:
    c.send(b"Data is corrupted - Checksum failed")

c.close()
s.close()