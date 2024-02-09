def text_to_morse(text):
    #creating dictionary for morsecode as it is
    morse_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..', ' ': '/'
    }

    morse_text = []
    for char in text.upper():
        if char in morse_dict:
            morse_text.append(morse_dict[char])
        else:
            morse_text.append(char)  #if not in my morse dict

    return ' '.join(morse_text)

input_text = input('Text to morse: ')
morse_result = text_to_morse(input_text)
print(f"The Morse code for '{input_text}' is: {morse_result}")