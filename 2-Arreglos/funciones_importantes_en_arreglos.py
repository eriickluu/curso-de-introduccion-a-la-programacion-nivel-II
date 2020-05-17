colors = ["Verde","Rojo","Azul"]
numbers = [1,2,3,4,5]
person = {"name":"Erick","lastName":"Lucio","age":20}
animal = {"name":"ozzy","color":"blanco","age": 4}

print(colors.pop(2))

colors.append("Amarrillo")

colors.insert(0,"Negro")

colors.remove("Verde")

print(colors.count("Negro"))

numbers.reverse()

numbers.extend(colors)

colors[2] = "Amarrillo fuerte"

print(person.pop("lastName"))

person.update({"telefono":"122222"})

person.update(animal)

print(len(person))

for value in colors:
    print(value)

for value in numbers:
    print(value)

for key, value in person.items():
    print(key," ",value)