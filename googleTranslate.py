from googletrans import Translator

tarjimon = Translator()

message = 'english to korean free translator. exit: stop:'

while True:
    text = input(message)
    if text == 'stop':
        break
    else:
        tarjima = tarjimon.translate(text,src='english', dest='korean')
        print(tarjima.text)