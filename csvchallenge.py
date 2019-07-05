import csv
from datetime import datetime
 

file = open("/Users/knuchegbu/Desktop/Grainger.csv", "r")
reader = csv.reader(file)

header = next(reader) # the first line is the header

data = ['lookup_key' for row in reader]
print (data)

# ['lookup_key', 'lookup_value', 'lookup_id', 'lookup_value2', 'vendor_xref_id']

