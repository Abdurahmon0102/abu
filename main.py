from googletrans import Translator


translator = Translator()

result = translator.translate('hi', dest = 'uz').text

print(result)


while True:
    text = input('inter text to translate')
    to_language = input('inter language to translate')

    result = translator.translate (text, to_language).text

    print(result)



