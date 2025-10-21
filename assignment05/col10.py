students = {"Alice": 3, "Bob": 5, "Charlie" : 2}
print(students)

name = input("Kirjoita yhden opiskelijan nimi: ")

keys = students.keys()

if name in keys:
    print(students.get(name))
else:
    print("Opiskelijaa ei löytynyt.")