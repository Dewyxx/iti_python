names = ["ahmed", "fatma", "Ibrahim"]
name_dict = {}
for name in names:
    first_char = name[0].lower()
    if first_char in name_dict:
        name_dict[first_char].append(name)
    else:
        name_dict[first_char] = [name]
print(name_dict)