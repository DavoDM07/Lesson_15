#Write a function that removes an element at a specified index from a list. Handle the
#IndexError by raising a custom exception if the index is out of range.

def element_replacement(text,index1,index2):
    if len(text) - 1 < index2:
        raise IndexError('Out of range')
    if index1 < 0:
        raise IndexError('The index must be over 0')
    my_replace = text.replace(text[index1:index2], "")
    return my_replace
print(element_replacement('BDG is the best company ever',4,20))
