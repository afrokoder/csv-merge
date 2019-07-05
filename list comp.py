#use a for loop to iterate through the series of items in alist 

companies = [
  {
    "name": "Bitcoin",
    "active": 0,
    "owner": "Satoshi"
  },
  {
    "name": "Iota",
    "active": 1,
    "owner": "Jaylen"
  },
  {
    "name": "Kraft",
    "active": 0,
    "owner": "Jackie"
  },
  {
    "name": "Apple",
    "active": 1,
    "owner": "Steve"
  }
]
new_comp =[company['owner'for company in companies:
    print 