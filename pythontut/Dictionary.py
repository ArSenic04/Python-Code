"""
Dictionary
"""
d1 = {"Shivam": "Pizza", "Arsenic": "Burger", "mummy": "roti", "daddy": "Kichadi",
      "Family": {"b": "bhakari", "l": "dal", "d": "timepass"}}
print(d1["Family"]["l"])

d1["baa"] = "magaj"
# This will be added at the last
print(d1)
# del is used to delete the part of dictionary
del d1["baa"]
print(d1)
for i in d1:
    print(i, d1[i])
