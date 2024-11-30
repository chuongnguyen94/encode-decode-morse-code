from data import MORSE_DICT

#ENCODING TEXT
text = input("Type your words: ").upper()
encoded_text = [MORSE_DICT[letter] for letter in text if letter != " "]
encoded_result = " ".join(encoded_text)
print(encoded_result)

#DECODING TEXT
decoded_text = []
for each in encoded_result.split(' '):
    for key in MORSE_DICT:
        if MORSE_DICT[key] == each:
            decoded_text.append(key)
decoded_spaced_text = []
if " " in text:
    space_index = text.index(' ')
    for each in decoded_text:
        if decoded_text.index(each) == space_index:
            decoded_spaced_text.append(' ')
        decoded_spaced_text.append(each)
else:
    decoded_spaced_text = decoded_text
decoded_result = "".join(decoded_spaced_text)
print(decoded_result)