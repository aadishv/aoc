txt = open("in.txt").read().split("\n")
l1 = []
l2 = []
for l in nums:
    s = l.split("   ")
    if len(s) == 2:
        l1.append(int(s[0]))
        l2.append(int(s[1]))

score = 0
for i in l1:
    c = len([j for j in l2 if j == i])
    score += i * c
print(score)
