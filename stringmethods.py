name,char = input("enter name and character: ").split(",")
print(f"length is :{len(name.replace(' ', ''))}")
print(f"count of character is = {name.replace(' ', '').lower().count(char.replace(' ', '').lower())}")
# replace is used to eleminate all the spaces 