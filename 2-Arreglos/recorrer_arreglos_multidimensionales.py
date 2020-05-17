shoes = {
    "Nike":["Tenis1","Tenis2","Tenis3"], 
    "Adidas":["Tenis4","Tenis5","Tenis6"], 
    "Converse":["Tenis7","Tenis8","tenis9"]}


for key, listt in shoes.items():
    for value in listt:
        print("Estos son los tenis", key, value)
