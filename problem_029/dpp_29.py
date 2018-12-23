def encode(word):
    word_len = len(word)
    if word_len<1:
        return ""
    i = 0
    counter = 0
    char = word[0]
    encoded_string = ""
    while i < word_len:
        if word[i] == char:
            counter +=1
        else:
            encoded_string += str(counter)
            encoded_string += char
            char = word[i]
            counter = 1
        i+=1
    encoded_string += str(counter)
    encoded_string += char
    return encoded_string


def decode(encoded_word):
    word_len = len(encoded_word)
    i = 0
    decoded_word = ""
    num_string = ""
    while i<word_len:
        if not encoded_word[i].isalpha():
            num_string +=encoded_word[i]
        else:
            number = int(num_string)
            for j in range(number):
                decoded_word += encoded_word[i]
            num_string = ""
        i+=1
    return decoded_word


test_words = ["AAAABBBCCDAA", "", "FARTERPARTER", "AAA"]
for i in test_words:
    encode_print = encode(i)
    decode_print = decode(encode_print)
    print(i)
    print(encode_print)
    print(decode_print)
    print()
