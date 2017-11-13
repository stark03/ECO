
import csv
import gzip
import io


with gzip.open("reviews_Cell_Phones_and_Accessories_5.json.gz", "r") as file:
    reader = csv.reader(io.TextIOWrapper(file, newline=""))
    print(list(reader))