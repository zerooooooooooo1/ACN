import socket

s = socket.socket()
s.connect(("localhost", 9999))

filename = input("Enter file name: ")
s.send(filename.encode())

data = s.recv(4096).decode()

print("\nFile contents:")
print(data)

s.close()