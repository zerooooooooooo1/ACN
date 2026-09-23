def crc(data):
    crc = 0xFFFF

    for byte in data.encode():
        crc ^= byte << 8

        for i in range(8):
            if crc & 0x8000:
                crc = (crc << 1) ^ 0x1021
            else:
                crc <<= 1

            crc &= 0xFFFF

    return crc


data = input("Enter data: ")

value = crc(data)

print("CRC-CCITT: ", hex(value))

# Verification
received = input("Enter CRC to verify (hex): ")

if int(received, 16) == value:
    print("Data is correct")
else:
    print("Data is corrupted")