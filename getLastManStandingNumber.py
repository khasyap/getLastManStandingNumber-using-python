def getLastManStandingNumber(n, k):
    survivor = 0
    for i in range(1, n + 1):
        survivor = (survivor + k) % i
    return survivor + 1

# Taking input from user
n, k = map(int, input().split())

# Printing output
print(getLastManStandingNumber(n, k))
