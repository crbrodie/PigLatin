pyg = 'ay'


answer = 'y'
while answer[0].lower() == 'y':
    original = input('Enter a word:')
    if len(original) > 0 and original.isalpha():
        word = original.lower()
        first = word[0]
        new_word = word[1:]+ first + pyg
        print(new_word)
        answer= input('Try a new word(Y/N)? ')
    else:
        print('empty')
else:
    print('Come back soon!')