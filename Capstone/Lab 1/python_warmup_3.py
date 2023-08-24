input_sentence = input("Enter a sentence: ")

def to_camel_case(sentence):
    words = sentence.split()  # will split everything I put here into words
    camel_words = [words[0].lower()] + [word.capitalize() for word in words[1:]]
    camel_case = ''.join(camel_words)
    return camel_case


camel_case_output = to_camel_case(input_sentence)
print("Camel case output:", camel_case_output)
