import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(("localhost", 9998))

data, addr = s.recvfrom(1024)

print("Message from Server:", data.decode())

s.close()