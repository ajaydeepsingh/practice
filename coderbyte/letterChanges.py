def LetterChanges(str):
    result = ""
    for char in str:
        if char.isalpha():
            char = chr(ord(char) + 1);
            if char == 'a':
                char = char.upper()
            elif char == 'e':
                char = char.upper()
            elif char == 'i':
                char = char.upper()
            elif char == 'o':
                char = char.upper()
            elif char == 'u':
                char = char.upper()
        result = result + char
    return result

# keep this function call here
print(LetterChanges("hello*3"))
print(LetterChanges("fun times!"))
