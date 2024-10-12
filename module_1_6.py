my_dict = {"Devil may cry": 2001, "Tomb Raider": 1996, "Tekken": 1994, "Mortal Kombat": 1992, "Mirror’s Edge": 2007}
print(my_dict)
print(my_dict["Devil may cry"])
my_dict["Castlevania"] = 1986 #обращаемся к несущ. ключу
print(my_dict)
my_dict.update({"Diablo": 1996, "Prince of Persia: Warrior Within": 2004})
print(my_dict)
del my_dict ["Mortal Kombat"]
print(my_dict)
print(my_dict.get ("Mortal Kombat"))
print(my_dict)

my_set = {9, 8, 7, 6, 5, 7, 6, 5, 4, "Cherry", False, (5, 4, 3)}
print(my_set)
my_set.update({10.52, True})
print(my_set)
print(my_set.discard("Cherry"))
print(my_set)