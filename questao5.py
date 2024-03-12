def reverse_string(text: str) -> str:
    reversed_string = list(text)

    text_length = len(text)
    half = int(text_length / 2)

    for i in range(half):
        aux = reversed_string[i]
        reversed_string[i] = reversed_string[text_length - 1 - i]
        reversed_string[text_length - 1 - i] = aux

    return ''.join(reversed_string)


text = input()
print(reverse_string(text))