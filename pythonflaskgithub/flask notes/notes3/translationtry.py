from translate import Translator
translator = Translator(to_lang="he")

with open('translator.txt') as trans:
    text = trans.readlines()
    for lines in text:
        new_string = translator.translate(lines)
        print(lines)
        print(new_string)



