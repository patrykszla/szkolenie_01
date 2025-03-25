# python 3.10 wprowadzony match case

lista = []
lang = input("Podaj znany Ci język programowania")
match lang.strip().casefold():
    case "php":
        lista.append("Znam php")
    case "js":
        lista.append("Znam Jave")
    case _:
        print("Nie znam nic :(")

print(lista)
