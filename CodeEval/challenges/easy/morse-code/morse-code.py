import sys


MORSE_ALPHABET = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
    '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
    '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9'
}


def decode_morse(morse_code):
    decoded_message = str()
    morse_words = morse_code.split("  ")
    for word in morse_words:
        for morse_letter in word.split(" "):
            decoded_message += MORSE_ALPHABET[morse_letter]
        decoded_message += " "

    return decoded_message.strip()

test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    if not test:
        continue

    morse_code = test.strip()
    print(decode_morse(morse_code))


test_cases.close()

