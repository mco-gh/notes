import json
import html2markdown

fields = ('title', 'author')

with open('clips.json') as file:
  data = json.load(file)

for i in data:
  print('link:', i)
  for j in fields:
    print(j + ': ', data[i][j])
  for j in data[i]['quotes']:
    print('content: ', html2markdown.convert(j['text']))
