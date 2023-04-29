dic = {
    "musicas": [
        {"nome": "Hey Jude", "banda": "Beatles"},
        {"nome": "November Rain", "banda": "Guns N' Roses"},
        {"nome": "How Deep Is Your Love", "banda": "Bee Bees"},
    ],
    "filmes": {
        "X-men": ["Wolverine", "Xavier", "Tempestade", "Vampira",
                  "Magneto", "Ciclope", "Gambit"],
        "Avengers": ["Homem de Ferro", "Hulk", "Thanos",
                     "Capitao America", "Thor", "Capitâ Marvel",
                     "homem aranha"],
        "Star Wars": ["Luke", "Leia", "C-3PO", "Dart Vader",
                      "Obi-Wan", "Yoda", "R2-D2", "Han Solo", "Chewbaca"]
    }
}


def func1(a, b, c, d):
    for x in a:
        if x[b] == d:
            return x[c]
    return "nãosei"


# print(dic["musicas"][0]["banda"] == "Beatles")
# print(func1(dic["musicas"], "banda", "nome", "Hey Jude") == "Beatles")
# print("Super-homem" in dic["filmes"]["Avengers"])
# print(dic["musicas"][2]["nome"] == "How Deep Is Your Love")
# print("Han Solo" in dic["filmes"]["Star Wars"])
# print("November Rain" == dic["musicas"][1]["banda"])
# print("Han Solo" in dic["jogos"]["Star Wars"])
# print("Homem de Ferro" in dic["musicas"][2])
# print(func1(dic["musicas"], "banda", "nome", "Guns N' Roses") == "November Rain")
# print(dic["filmes"]["X-men"][3] == "Vampira")
print("Hey Jude" in dic["musicas"]["Beatles"])