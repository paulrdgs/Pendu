import random

words = "coucou rouge terre choucroute france portable ordinateur hachette zeubi louange"
words_list = words.split()

secret = random.randint(0, len(words_list) - 1)
secret_word = words_list[secret]

game = {
    "secret_word": secret_word,
    "guess_word": "_" * len(secret_word),
    "life": 9
}

print(f'{ game["guess_word"] } | vie : { game["life"] }')

while True:
    letter = input('? > ')
    
    if letter.isalpha() == False:
        print("Veuillez taper une lettre !")
    elif letter in game["secret_word"] and letter not in game["guess_word"]:
        guess_word_list = list(game["guess_word"])
        for index, current_letter in enumerate(game["secret_word"]):
            if current_letter == letter:
                guess_word_list[index] = letter
        game["guess_word"] = "".join(guess_word_list)
    elif letter not in game["secret_word"] or letter in game["guess_word"]:
        game["life"] -= 1
    
    print(f'{ game["guess_word"] } | vie : { game["life"] }')

    if "_" not in game["guess_word"]:
        print("Vous avez gagné !")
        break
    elif game["life"] < 1:
        print("Vous avez perdu !")
        break