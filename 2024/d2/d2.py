txt = open("in.txt").read().split("\n")
t = 0
def checkIfSafe(n):
    if len(n) > 1:
        isTrue = True
        increasing = n[0] > n[1]
        for j in range(len(n)-1):
            if n[j] == n[j+1]:
                isTrue = False
            if (n[j] > n[j+1]) != increasing:
                isTrue = False
            if not (1 <= abs(n[j]-n[j+1]) <= 3):
                isTrue = False
        return isTrue
    return False
for i in txt:
    n = [int(j) for j in i.split(" ") if j != ""]
    if checkIfSafe(n):
        t += 1
    else:
        for i in range(len(n)):
            if checkIfSafe(n[:i] + n[i+1:]):
                print(n, i)
                t += 1
                break
print(t)
