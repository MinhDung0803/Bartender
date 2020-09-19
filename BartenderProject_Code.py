import random
question = {"strong": "Do ye like yer drinks strong?",
            "salty": "Do you like with a salty tang?",
            "bitter": "Are you a lover who likes it bitter?",
            "sweet": "Would you like a bit of sweetness with your poison?",
            "fruity": "Are you one of a fruity finish?"
            }

ingredients = {"strong": ["glug of rum","slug of whisky","splash of gin"],
               "salty": ["olive on a stick","salt-dusted rim","rasher of bacon"],
               "bitter": ["shake of bitter","splash of tonic","twist of lemon peel"],
               "sweet": ["sugar cube","spoonful of honey","spash of cola"],
               "fruity": ["slice of orange","dash of cassis","cheery on top"]
               }
def bartender():
    string = input("Hello Sir, What would you like to drink, please?"+".\n"
                   "We have these flavours, please choose one as your favorite:"+"\n"
                   "strong, salty, bitter, sweet, fruity"+"\n"
                   "Please enter your favorite flavour: ")

    if string in question:
        print(question[string])

    yesno = input("Please answer this question to confirm your drinks flavour(Yes or No): ")

    if yesno == "yes":
        flavour = ingredients[string]
        rd = random.randint(0, 2)
        print("We recommend this drinks: ",flavour[rd])
    else:
        print("Please choose your drink's flavour again")

bartender()

