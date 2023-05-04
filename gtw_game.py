import random

words = ['agua', 'comodin', 'aplicacion', 'matrimonio', 'responsabilidad', 'animal', 'raton', 'acertijo', 'inferir', 'asimilar']
finished = False
trys = 0
num_words = len(words)-1

word_index = random.randint(0, num_words)

selected_word = words[word_index]
word_lenght = len(selected_word)

guess = ''
for i in range(word_lenght):
    guess = guess + '_ '
guess = guess + '\n'

guessing = input(guess)

# print(selected_word)
# print(word_lenght)
while finished == False and trys < 4:
    guess = ''
    for i in range(word_lenght):
        if guessing[i] == selected_word[i]:
            guess = guess + guessing[i]
        elif guessing[i] in selected_word:
            guess = guess + guessing[i] + '*'
        else:
            guess = guess + '_ '
    guess = guess + '\n'

    guessing = input(guess)

    if guessing == selected_word:
        finished = True
        print('Felicidades, has acertado, la palabra era: ' + str(selected_word))
    trys = trys + 1

if trys >= 4:
    print('Lo siento, no lo has conseguido, la palbra era: ' + str(selected_word))