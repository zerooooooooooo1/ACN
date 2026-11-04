
import xmlrpc.client

s = xmlrpc.client.ServerProxy("http://localhost:8000/")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operation (+,-,*,/): ")

try:
    if op == '+': print("Result:", s.add(a, b))
    elif op == '-': print("Result:", s.sub(a, b))
    elif op == '*': print("Result:", s.mul(a, b))
    elif op == '/': print("Result:", s.div(a, b))
    else: print("Invalid operation")
except Exception as e:
    print("Error:", e)
