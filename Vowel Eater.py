''' A simple vowel eater that uses
a for loop;
the concept of conditional execution (if-elif-else)
and the continue statement.'''

user_word = str(input("Enter any word:"))
user_word = user_word.upper()
vowels = ('A','E','I','O','U')
for letter in user_word:
    if letter in vowels:
        continue
    elif letter == vowels:
        letter = letter - vowels
    else:
        print(letter)
