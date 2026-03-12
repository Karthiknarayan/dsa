n = int(input())

arr = list(map(int, input().split()))

hash = [0] * (n+1)

# precompute
for i in range(n):
    hash[arr[i]] += 1

print("fetching hash.....")

for i in range(n):
    print(hash[arr[i]])