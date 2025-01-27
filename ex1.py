#Write a function that checks the length of a string provided by the user. Handle the
#TypeError by raising a custom exception if the input is not a string.

def checking_text_type(text):
    if type(text) != str:
        raise TypeError('Sorry the text does not fully match the string')
    print(len(text))
checking_text_type('BDG is the best company ever')

