def countvowel(text):
    vowels = "aeiuo"
    print(len([letter for letter in text if letter in vowels]))
    print([letter for letter in text if letter in vowels])
countvowel('hellothere');
