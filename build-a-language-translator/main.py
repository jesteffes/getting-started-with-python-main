translations = {
  "hello":"hola",
  "thank you":"gracias",
  "sorry":"lo siento",
  "i am a woman":"yo soy una mujer",
  "the man":"el hombre",
  "excuse me":"disculpe",
  "you are welcome":"de nada",
  "can you bring me an extra glass":"me puede traer un vaso extra",
  "i love cheese":"me encanta el queso"
}

done = False

print('Type "done" at any time to exit')


while not done:
    word = input("Type an English word to translate: ")
    word = word.lower()

    if word == "done":
        done = True
    elif word in translations:
        print(translations[word])
    else:
        print("Translation is not known")