import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(("localhost", 9999))

print("Server started...")
s.sendto(b"Hello from Server!", ("localhost", 9998))

s.close()