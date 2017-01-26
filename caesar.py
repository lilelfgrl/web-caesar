def alphabet_position(letter):
    letter = letter.lower()
    return ord(letter) - 97
def rotate_character(character,rotation):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if character.isalpha() == False:
        return character
    elif character in alphabet:
        rotated_index = alphabet_position(character) + rotation
        if rotated_index < 26:
            return alphabet[rotated_index]
        else:
            return alphabet[rotated_index % 26]
    elif character in alphabet2:
        rotated_index = alphabet_position(character) + rotation
        if rotated_index < 26:
            return alphabet2[rotated_index]
        else:
            return alphabet2[rotated_index % 26]


def encrypt(text,rot):
    position = 0
    output_string = ""
    while(position < len(text)):
        newchar = rotate_character(text[position],rot)
        output_string = output_string + newchar
        position = position + 1
    return output_string
