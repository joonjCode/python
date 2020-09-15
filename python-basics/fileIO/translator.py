from translate import Translator


translator = Translator(to_lang='ja')
try:
    with open('test.txt', 'r') as f:
        text = f.read()
        translation = translator.translate(text)
        # print(translation)
        with open('test-ja.txt', 'w') as f2:
            f2.writelines(translation)
except Exception as e:
    raise FileNotFoundError('File does not exist')
