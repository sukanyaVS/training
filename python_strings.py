#Write a program to create a new string made of an input string’s first, middle, and last character.?
my_word = str(input("Enter any word : "))
x = len(my_word) / 2
y = int(x)
new_word = print("New word : " ,my_word[0] + my_word[y] + my_word[-1])


#write a program to count occurrences of all characters within a string?'
word = "malayalam"

def cout_letters(word):
    unique_val = set(word)
    for i in unique_val:
      count = word.count(i)
      print("Count of",i,":",count)

cout_letters(word)