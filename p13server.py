
from xmlrpc.server import SimpleXMLRPCServer

def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b):
    if b == 0: raise ZeroDivisionError("Cannot divide by zero")
    return a // b

s = SimpleXMLRPCServer(("localhost", 8000))
s.register_function(add)
s.register_function(sub)
s.register_function(mul)
s.register_function(div)

print("Server running...")
s.serve_forever()
