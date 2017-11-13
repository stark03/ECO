import gzip
import simplejson
import csv
import plotly
plotly.tools.set_credentials_file(username='TusharMurarka', api_key='uMzgn8HNc9ah29sW64k0')
from matplotlib import style
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.tools import FigureFactory as FF
import operator as op
import re
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


list_of_dicts = []
with open('people.csv','r') as f:
    reader = csv.DictReader(f)
    for line in reader:
        list_of_dicts.append(line)

m = []
r = []
wordcount = []
complexWordCount = []
read = []
quad = []
star = []

for item in list_of_dicts:
  m.append(item['helpful'])

for i in m:
  t = re.findall('\d+',i)
  if t[0] == '0' or t[1] == '0':
    r.append(0.0)
  else:
    i1 = float(t[0])
    i2 = float(t[1])
    r.append(i1/i2)


for i in list_of_dicts:
  p = i['reviewText']
  q = i['summary']
  pl = len(p.split())
  ql = len(q.split())
  wordcount.append(pl)
  complexWordCount.append(ql)


for d,num in zip(list_of_dicts,r):
        d['vall'] = num
        d['quadratic'] = float(d['overall'])*float(d['overall'])
        

for d,num in zip(list_of_dicts,wordcount):
        d['wordcount'] = num

for d,num in zip(list_of_dicts,complexWordCount):
        d['complexWordCount'] = num

j = len(wordcount)

for i in range(0,j):
        if wordcount[i]!= 0:
          p = 0.4*float(100*((float(complexWordCount[i]))/float(wordcount[i])) + 8)
        else:
          p = 3.2
        read.append((100/p))
        #print(100/p)

for d,num in zip(list_of_dicts,read):
        d['fogIndex'] = num


ratio = []

keys = list_of_dicts[0].keys()
with open('out.csv','wb') as f:
    writer = csv.DictWriter(f, keys)
    writer.writeheader()
    writer = csv.DictWriter(f,fieldnames=list_of_dicts[0].keys())
    for i in list_of_dicts: 
        writer.writerow(i)

list_of_dicts.sort(key=op.itemgetter('wordcount'))

for i in list_of_dicts:
  star.append(i['wordcount'])
  quad.append(i['quadratic'])
  ratio.append(i['vall'])
print(len(ratio))


fig = plt.figure()
ax1 = fig.add_subplot(111)

#ax1.bar(ratio,star)
style.use('ggplot')
plt.plot(star,ratio)
plt.ylim(-1.5,1.5)
plt.xlim(0,300)
plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()