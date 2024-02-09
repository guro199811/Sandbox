
morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', ' ': '/'
}

def morse_to_text(morse_code):
    # Creating the reverse dictionary for Morse code
    reverse_morse_dict = {v: k for k, v in morse_dict.items()}

    # Split the Morse code by spaces to get individual characters
    morse_words = morse_code.split(' ')
    decoded_text = []

    for morse_word in morse_words:
        if morse_word == '/':
            # Handle spaces between words
            decoded_text.append(' ')
        else:
            # Look up the Morse code in the reverse dictionary
            decoded_char = reverse_morse_dict.get(morse_word, morse_word)
            decoded_text.append(decoded_char)

    return ''.join(decoded_text)

# Example usage:
morse_input = input('Morse code to decode: ')
decoded_result = morse_to_text(morse_input)
print("decoded_result")