# Simple version following your guidelines exactly

print("Type a sentence ending with '.': ")
sentence = input()

length = 0
words = 0
vowels = 0
in_word = False

for char in sentence:
    length += 1  # Count every character
    
    # Check vowel
    if char.lower() in "aeiou":
        vowels += 1
    
    # Check for words
    if char == ' ' or char == '.':
        if in_word:
            in_word = False
    else:
        if not in_word:
            in_word = True
            words += 1
    
    # Stop at point
    if char == '.':
        break

print(f"Length: {length}")
print(f"Words: {words}")
print(f"Vowels: {vowels}")