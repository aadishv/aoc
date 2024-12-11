import re
LESSON = 2
myregex = re.compile(r"([\u4e00-\u9fff]+)\s+?([\u4e00-\u9fff]+)")
#
x = ' '.join(open('icl1p1.txt').read().split('\n'))
r = re.findall(myregex, x)
print(r)
exit()
n = 0
words = []
for traditional, simplified, pinyin, particle, definition, lesson in r:
    if lesson.strip() == '1':
        words.append((simplified.strip(), pinyin.strip().lower(), definition.strip()))
        n += 1
supplemental = open('supplemental.txt').read().strip().split('\n\n')
swords = []
while supplemental != []:
    w = (supplemental.pop(0).strip(), supplemental.pop(0).strip(), supplemental.pop(0).strip())
    if len([i for i in words if words[0] == w[0]]) == 0:
        swords.append(w)
        n += 1

for i in words:
    print(i[2])
    print(f'{i[0]} ({i[1]})')
    print(f'tags: l{LESSON}')
    print()
for i in swords:
    print(i[2])
    print(f'{i[0]} ({i[1]})')
    print(f'tags: l{LESSON} supplemental')
    print()
