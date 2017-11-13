import gzip
import csv


def parse(path):
  g = gzip.open(path, 'r')
  for l in g:
    yield eval(l)

k = []
for e in parse("reviews_Cell_Phones_and_Accessories_5.json.gz"):
 	k.append(e)

l = []
l = k[:100]
keys = l[0].keys()
with open('people.csv', 'wb') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(l)