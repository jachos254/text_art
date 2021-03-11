import random

from alphabet import alphabet


def get_string():
    string = input('Proszę swoje wypociny: ')
    return string

# string = 'No ja nie, . wiem jak on to robi: Maciek króci no!'

def doit():
    string = get_string()
    new_word = []
    lowered = string.lower()
    letters = list(lowered)
    for letter in letters:
        if letter in alphabet:
            new_word.append(alphabet[letter][random.randrange(len(alphabet[letter]))])
        else:
            new_word.append(letter)
    final_word = ''.join(new_word)
    print(final_word)

if __name__ == '__main__':
   while True:

        doit()



