import re

myregex = re.compile(r"([\u4e00-\u9fff]+)\s+([\u4e00-\u9fff]+)\s+(.+?)\s+(adj|adv|conj|interj|m|mv|n|nu|p|pn|prep|pr|qpr|t|v|vo|vc)\s+(.+?)\s+(\d{1,2})")
#
x = ' '.join(open('test.html').read().split('\n'))
r = re.findall(myregex, x)
print(len(r))
n = 0
for traditional, simplified, pinyin, particle, definition, lesson in r:
    if lesson.strip() == '1':
        print(simplified, pinyin, definition)
        n += 1
print(n)
