
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('localhost', 5000))

data, addr = s.recvfrom(1024)
msg, c = data.decode().rsplit('|', 1)

checksum = (~sum(msg.encode())) & 0xFFFF

print("Received Data:", msg)
print("Received Checksum:", c)

if checksum == int(c):
    print("No Error Detected")
else:
    print("Transmission Error Detected")
