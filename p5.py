size = int(input("Enter packet size: "))
mtu = int(input("Enter MTU: "))

header = 20
data = mtu - header
offset = 0
fragments = []

while size > 0:
    length = min(data, size)
    fragments.append((offset, length))
    print("Fragment: Data =", length, "Offset =", offset)

    offset += length
    size -= length

print("\nReassembly:")
total = 0

for offset, length in fragments:
    print("Offset =", offset, "Data =", length)
    total += length

print("Original packet reassembled. Total data =", total)