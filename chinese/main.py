import json
ic = []
for i in range(5):
    ic += json.load(open(f'gemini_ic/{i+1}.json'))
for word in ic:
    print('front-text:', word['english'])
    print(f'back-text: {word['characters']} ({word['pinyin']})')
    print(f'tags: l{word['lesson']}')
    print()
