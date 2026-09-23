import socket

s = socket.socket()
s.bind(("localhost", 9999))
s.listen(1)

print("Server waiting...")

conn, addr = s.accept()

filename = conn.recv(1024).decode()
print("Requested file:", filename)

try:
    with open(filename, "r") as f:
        data = f.read()
    conn.send(data.encode())
except:
    conn.send(b"File not found")

conn.close()
s.close()