def reverse(text):
    result = ""
    for i in range(-1, -1*(len(text) + 1), -1):
        result += text[i]

    return result
