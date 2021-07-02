name = ["Sagnik", "Mitra"]
newlist = []
for x in name:
    if "Sagnik" in name:
        newlist.append(x)
print(newlist)
newlist1 = [x for x in name if "Sagnik" in x]
