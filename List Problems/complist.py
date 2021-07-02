name = ["Sagnik", "Mitra"]
newlist = []
for x in name:
    if "Sagnik" in name:
        newlist.append(x)
print(newlist)
newlist2 = [x for x in name if "Sagnik" in x]
