name = ["Sagnik", "Meenu", "Abhishek", "Aditya"]
regular_list_syntax = []
comp_list_syntax = []
for i in name:
    if "a" in i.lower():
        regular_list_syntax.append(i)
print(regular_list_syntax)

comp_list_syntax = [i for i in name if "a" in i]
print(regular_list_syntax)
