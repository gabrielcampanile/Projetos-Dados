def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')


greet('en')

greet('es')

greet('fr')

print(greet('es'), ', Anna')
