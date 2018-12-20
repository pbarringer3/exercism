def is_pangram(sentence):
    sentence = sentence.lower()
    sentence_set = set(sentence)

    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    full_set = set(alphabet)

    return alphabet <= sentence_set
