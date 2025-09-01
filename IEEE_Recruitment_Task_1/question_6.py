cutoffList = [
("Pilani", "CS", 327),
("Pilani", "Chemical", 247),
("Pilani", "Msc. Eco", 271),
("Pilani", "Msc.Bio", 236),

("Goa", "CS", 301),
("Goa", "Chemical", 239),
("Goa", "Msc. Eco", 263),
("Goa", "Msc.Bio", 234),

("Hyderabad", "CS", 298),
("Hyderabad", "Chemical", 238),
("Hyderabad", "Msc. Eco", 261),
("Hyderabad", "Msc.Bio", 234),
]

print("Cutoff List:")
print(cutoffList)

cutoffDict = dict(Pilani={}, Goa={}, Hyderabad={}) # intialize a dict of dicts with the campuses as the keys

for c in cutoffList:
    cutoffDict[c[0]][c[1]] = c[2] # fill the dict with values from the list

print("\nCutoff dictionary:")
print(cutoffDict)
