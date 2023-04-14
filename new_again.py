def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    display_word = ''
    for i in secret_word:
        if i in display_word:
            continue
        elif i in letters_guessed:
            display_word += i
            #print(display_word)
        else:
            display_word += '_ '
            #print(display_word)
    return display_word
    print(display_word)
#
#a = 'apple'
#b = ['e','i','k','p','r','s']
#print(get_guessed_word(a,b))


word = 'elephant'
guesses = 6
num_letters = len(word)
print('the no. of letters is ',len(word))

l_guess =[]
new_word = get_guessed_word(word,l_guess)
print(new_word)

while guesses >0:
    guess = input('enter a guess')
    l_guess.append(guess)
    print(get_guessed_word(word,l_guess))
    
print('thanks for seeing ")
