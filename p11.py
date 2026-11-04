
n = int(input("Enter number of packets: "))
cap = int(input("Enter bucket capacity: "))
rate = int(input("Enter output rate: "))

bucket = 0

for i in range(n):
    p = int(input("Enter packet size: "))

    if bucket + p <= cap:
        bucket += p
        print("Packet accepted")
    else:
        print("Packet discarded")

    sent = min(bucket, rate)
    bucket -= sent
    print("Transmitted:", sent, "Remaining:", bucket)

while bucket:
    sent = min(bucket, rate)
    bucket -= sent
    print("Transmitted:", sent, "Remaining:", bucket)
