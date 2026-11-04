
n = int(input("Enter number of routers: "))
print("Enter cost matrix (999 for infinity):")
g = [list(map(int, input().split())) for _ in range(n)]

s = int(input("Enter source router: "))
d = [999] * n
v = [0] * n
d[s] = 0

for _ in range(n):
    u = min((d[i], i) for i in range(n) if not v[i])[1]
    v[u] = 1

    for j in range(n):
        if not v[j] and d[u] + g[u][j] < d[j]:
            d[j] = d[u] + g[u][j]

print("Shortest distances:")
for i in range(n):
    print(s, "to", i, "=", d[i])
