glossario = {'title': 'deixa a primeira letra maiúscula',
             'str': 'torna o valor da string literal',
             'if': 'se o valor da condição for verdadeiro',
             'elif': 'é executado se caso if for falso',
             'else': ' normalmente executado após alguma string'}
for significado in glossario:
    print('\nSignificado de: '
          + significado.title()
          + ': '
          + glossario[significado])
