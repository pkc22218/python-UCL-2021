"""
COMP0015 Samoan
"""

def play_again():
    """
    Ask the user whether they want to enter a word.
    Return True if they do and False if not.
    """
    valid_input = False

    again = True

    while not valid_input:
        answer = input("Do you want to enter another word? Y/YES/N/NO: ")
        first_char = answer[0].lower()
        if first_char in "yn":
            valid_input = True
            if first_char == 'y':
                again = True
            else: 
                again = False
        else:
            print("You typed: ", answer, "Try again.")

    return again


def get_word():
    """
    Get a word from the user and check if it contains valid characters from the 
    Samoan alphabet.
    Return a valid word.
    """
    valid  = False

    while not valid:
        word = input("Enter a word to pronounce: ").lower()
        char = check_valid_characters(word)
        if char != "":
            print(char.upper(), "is not a valid character")
            print()   
        else:
            valid = True        
    return word


def check_valid_characters(string):
    """
    Check that the characters in string contain valid characters from the
    Samoan alphabet. 
    Return the first invalid character or the empty string.
    """
    
    valid_char = ["f","m","n","p","s","t","v","l","g","a","i","e","o","u","'"," "]
    for i in range(len(string)):
        letter = string[i]
        if letter not in valid_char:
            return letter
    return ""

def phonetic_word(word):
    """
    Create a phonetic representation of word.
    Return the phonetic representation of word.
    """
    phonetic = ""
    consonant = 'fmnpstv'
    vowels = 'aeiou'
    double_vowels= ['ae','ai','ao','au','ei','eu','oi','ou','iu','ui']
    for i in range(0,len(word)):
        if word[i] in consonant:
            phonetic += word[i]
        elif word[i] in 'l' :
            if word [i-1] in 'aou' and word [i+1] in 'i': 
                phonetic += 'rah' 
                if i < len(word)-1:
                    if word[i] in " '":
                        phonetic += ' '
                    elif word[i] in "'":
                        phonetic += "'"
                    elif word[i+1] in " '":
                        pass
                    else:    
                        phonetic += '-'
            else:
                phonetic += 'l'   
        elif word[i] in 'g':
            phonetic += 'ng'
        elif word[i:i+2] in double_vowels :
            if word[i:i+2] in ['ae','ai']:
                phonetic += 'eye'
            elif word[i:i+2] in ['ao','au']:
                phonetic += 'ow'
            elif word[i:i+2] in ['ei']:
                phonetic += 'ay'
            elif word[i:i+2] in ['eu']:
                phonetic += 'eh-oo'
            elif word[i:i+2] in ['oi']:
                phonetic += 'oy'
            elif word[i:i+2] in ['ou']:
                phonetic += 'ow'
            elif word[i:i+2] in ['iu']:
                phonetic += 'ew'
            elif word[i:i+2] in ['ui']:
                phonetic += 'ooey'
            if i < len(word)-2:
                if word[i] in ' ':
                    phonetic += ' '
                elif word[i] in "'":
                    phonetic += "'"
                elif word[i+2] in " '":
                    pass
                else:    
                    phonetic += '-'
        else:          
            translate = True
            while translate:
                if word[i-1:i+1] in double_vowels and i-1 >= 0:
                    translate = False    
                else: 
                    translate = True
                    if word[i] in 'a':
                        phonetic += 'ah'
                    elif word[i] in 'e':
                        phonetic += 'eh'
                    elif word[i] in 'i':
                        phonetic += 'ee'
                    elif word[i] in 'o':
                        phonetic += 'oh'
                    elif word[i] in 'u':
                        phonetic += 'oo'
                    if i < len(word)-1:
                        if word[i] in ' ':
                            phonetic += ' '
                        elif word[i] in "'":
                            phonetic += "'"
                        elif word[i+1] in " '":
                            pass
                        else:    
                            phonetic += '-'
                    break    
    return phonetic          

def main():
    """
    Repeat the program until the user doesn't want to play
    """
    play = True
    
    while play:
        word = get_word()
        print(word.upper(), "is pronounced: ", end="")
        print(phonetic_word(word))
        play = play_again()


if __name__ == "__main__":
    main()
