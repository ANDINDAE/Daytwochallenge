def countvowel(text):
    vowels = "aeiuoAEIOU"
    print(len([letter for letter in text if letter in vowels]))
    print([letter for letter in text if letter in vowels])
countvowel('My name is Jamilla Kalungi Nassazi');